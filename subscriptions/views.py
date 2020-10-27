from django.shortcuts import redirect,render
from .forms import *
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse

class SubscribeView(LoginRequiredMixin,TemplateView):
	template_name='subscribe.html'
 
	def get(self,*args, **kwargs):
		context=self.get_context_data(**kwargs)
		context['form']=SubForm()
		if hasattr(self.request.user,'subscription'):
			context['subscribed']=True
			return render(self.request,self.template_name,context)
		context['subscribed']=False
		return render(self.request,self.template_name,context)

	def post(self,*args, **kwargs):
		form=SubForm(self.request.POST)
		sub=form.save(commit=False)
		sub.user=self.request.user
		sub.save()
		messages.success(self.request, 'Uspešno ste se pretplatili')
		return redirect(reverse('subscriptions:subscribe'))

@login_required
def unsubscribe(request,**kwargs):
	if not hasattr(request.user,'subscription'):
		return HttpResponseForbidden('Error 404')
	s=request.user.subscription
	s.delete()
	messages.error(request,'Pretplata je uspešno poništena!')
	return redirect(reverse('subscriptions:subscribe'))





		





