from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.decorators.http import require_POST
from .models import *
from django.utils import timezone
from .forms import *
from .decorators import *
from django.core.exceptions import PermissionDenied
from .query_functions import *
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator
# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cache_key='most_viewed'
		cache_value=cache.get(cache_key)
		if cache_value is None:
			posts=most_viewed_posts()
			cache.set(cache_key,posts)
		else:
			posts=cache_value
		context['posts']=posts
		return context

##############Topics##############################
class TopicCreate(UserPassesTestMixin,CreateView):
	model=Topic
	fields=['name']
	template_name_suffix='_create'#topic_create.html

	def test_func(self):
		return self.request.user.is_superuser

class TopicsList(ListView):
	model=Topic
	context_object_name='topics'

class TopicDelete(UserPassesTestMixin,DeleteView):
	model=Topic
	success_url=reverse_lazy('blog:topic_list')

	def test_func(self):
		return self.request.user.is_superuser

@method_decorator(cache_page(10),name='dispatch')
class TopicDetail(DetailView):
	model=Topic
	def get_context_data(self,**kwargs):
		 context = super().get_context_data(**kwargs)
		 posts=self.object.posts.exclude(published_date__isnull=True).only('title','published_date')
		 context['posts']=posts
		 return context

############POSTS##################################
class PostCreate(UserPassesTestMixin,CreateView):
	model=Post
	form_class=PostCreateForm

	def test_func(self):
		return self.request.user.is_staff
	def form_valid(self,form):
		kw=','.join(form.instance.tags)
		form.instance.meta_keywords=kw
		return super().form_valid(form)

class PostDetail(UserPassesTestMixin,DetailView):
	model=Post

	def test_func(self):
		post=Post.objects.get(pk=self.kwargs['pk'])
		if not post.published_date and not self.request.user.is_staff:
			return False
		return True 

	def get_object(self):
		post = super().get_object()
		if not self.request.user.is_staff:
			post.clicks=F('clicks')+1
			post.save()
		return post

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['comment_form']=CommentForm()
		context['comments']=self.object.comments.filter(post__pk=self.kwargs['pk'])[:3]
		return context

@require_POST
@login_required(redirect_field_name=reverse_lazy('blog:post_display'))
def add_comment(request,**kwargs):
	try:
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=Comment(text=form.cleaned_data['text'])
			post=Post.objects.get(pk=kwargs['pk'])
			comment.author=request.user.info
			comment.post=post
			comment.save()
			return redirect(reverse_lazy('blog:post_detail',
				kwargs=kwargs))
	except PermissionDenied:
		return HttpResponseForbidden('<h2>Greška! Verovatno ste prekoračili dnevni limit za komentare!</h2>')

def comment_list(request,**kwargs):
	try:
		post=Post.objects.get(pk=kwargs['pk'])
		comments=post.comments.all()
		paginator=Paginator(comments,10)
		page_number=request.GET.get('page')
		page_obj=paginator.get_page(page_number)
		return render(request,'blog/comment_list.html',{'page':page_obj,'post':post}) 
	except:
		return HttpResponseForbidden('<h2>Forbidden!</h2>')

@login_required
def comment_remove(request,**kwargs):
	try:
		comment=Comment.objects.get(pk=kwargs['pk'])
		if not (comment.author == request.user.info or request.user.is_superuser):
			return HttpResponseForbidden('<h2>Forbidden!</h2>')
		r_pk=comment.post.pk
		comment.delete()
		return redirect('blog:comment_list',pk=r_pk)
	except:
		return HttpResponseForbidden('<h2>Forbidden!</h2>')


@method_decorator(cache_page(10),name='get')
class UserPostsDisplay(TemplateView):
	template_name='blog/post_display.html'
	http_method_names=['get','post']

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['form']=SearchForm()
		return context
		context['get_method']=False

	def get(self,*args, **kwargs):
		context=self.get_context_data(**kwargs)
		posts=Post.published.all()
		paginator=Paginator(posts,10)
		page_number=self.request.GET.get('page')
		page_obj=paginator.get_page(page_number)
		context['page_obj']=page_obj
		context['get_method']=True
		return render(self.request,self.template_name,context)

	def post(self,*args, **kwargs):
		search=SearchForm(self.request.POST)
		context=self.get_context_data(**kwargs)
		if search.is_valid():
			key=search.cleaned_data['key']
			posts=post_search(key)
			context['page_obj']=posts
		return render(self.request,self.template_name,context)

class UnpublishedPostsDisplay(UserPassesTestMixin,ListView):
	queryset=Post.objects.filter(published_date__isnull=True)
	context_object_name='posts'
	paginate_by=10

	def test_func(self):
		return self.request.user.is_staff

@superuser_only
def publish(request,pk):
	post=get_object_or_404(Post,pk=pk)
	post.publish()
	return redirect('blog:post_detail',pk=pk)

class UpdatePost(UserPassesTestMixin,UpdateView):
	model=Post
	form_class=PostCreateForm
	template_name_suffix='_update'
	def test_func(self):
		return self.request.user.is_superuser

class PostDelete(UserPassesTestMixin,DeleteView):
	model=Post
	success_url=reverse_lazy('blog:post_display')

	def test_func(self):
		return self.request.user.is_superuser
###########################Preference######################
@require_POST
@login_required(redirect_field_name=reverse_lazy('blog:post_display'))
def add_pref(request,pk,value):
	try:
		if not (value == 'like' or value == 'dislike'):
			raise Exception('Unvalid value')
		author_pk=str(request.user.pk)
		post=Post.objects.get(pk=pk)
		prefs=post.preferences
		if author_pk not in prefs.keys():
			if value=='like':
				post.preferences[author_pk]='like'
				post.likes=F('likes')+1
			else:
				post.preferences[author_pk]='dislike'
				post.dislikes=F('dislikes')+1
		else:
			pref_value=prefs[author_pk]
			if pref_value=='like' and value=='dislike':
				post.preferences[author_pk]='dislike'
				post.likes=F('likes')-1
				post.dislikes=F('dislikes')+1
			if pref_value=='dislike' and value=='like':
				post.preferences[author_pk]='like'
				post.dislikes=F('dislikes')-1
				post.likes=F('likes')+1
		post.save()
		return redirect('blog:post_detail',pk=pk)
	except Exception as e:
		print('Greška tokom dodavanja recenzije',e)
		return HttpResponseForbidden()

@superuser_only
def manage_additionals(request,pk):
	post=Post.objects.get(pk=pk)
	images=ImagesFormset(instance=post,prefix='images')
	if request.method=='POST':
		images=ImagesFormset(request.POST, request.FILES,instance=post,prefix='images')
		images.is_valid() and images.save()
		return redirect('blog:post_detail',pk=pk)
	return render(request,'blog/additionals.html',{'images':images,})


