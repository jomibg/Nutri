from django.test import TestCase,Client
from ..models import Post,Topic,Comment
from model_bakery import baker
from datetime import date
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class TestPostViews(TestCase):
    @classmethod
    def setUpTestData(self):
    	self.t1=baker.make(Topic,name='Test123')
    	self.p1=baker.make(Post,published_date=None,topic=self.t1,text='example....')
    	self.posts=baker.prepare(Post,published_date=date.today(),_quantity=5,text='example....')
    	self.user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass",is_superuser=True,is_staff=True)

    def setUp(self):
        self.client=Client()

    def test_detail_view_redicrects(self):
    	response1=self.client.get(reverse_lazy('blog:post_detail',kwargs={'pk':self.p1.pk}))
    	self.assertRedirects(response1,'/accounts/login/?next=/blog/post/1')

    def test_detail_view(self):
    	self.client.force_login(user=self.user)
    	response2=self.client.get(reverse_lazy('blog:post_detail',kwargs={'pk':self.p1.pk}))
    	self.assertEqual(response2.status_code,200)

    def test_comment_add(self):
        data={'text':'test123...'}
        self.client.force_login(user=self.user)
        response=self.client.post(reverse_lazy('blog:comment_add',kwargs={'pk':self.p1.pk}),data=data)
        print(Comment.objects.get(post__pk=self.p1.pk))
        self.assertRedirects(response,reverse_lazy('blog:post_detail',kwargs={'pk':self.p1.pk}))

    def test_comment_delete_forbbiden(self):
        c2=Comment.objects.create(text='txt345',post=self.p1,author=self.user.info)
        response=self.client.get(reverse_lazy('blog:comment_delete',kwargs={'pk':c2.pk}))
        self.assertEqual(response.status_code,302)





