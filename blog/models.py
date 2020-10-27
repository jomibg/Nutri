from django.db import models
from django.contrib.postgres import fields
from datetime import date
from accounts.models import ProfileInfo
from django.urls import reverse
from froala_editor.fields import FroalaField
from .mixins import MetaTagBase,PublishedMenager
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Topic(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:topic_detail',kwargs={'pk':self.pk})

class Post(MetaTagBase):
	title=models.CharField(max_length=200)
	text=FroalaField(image_upload=True)
	topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,related_name='posts',
		null=True,blank=True)
	published_date = models.DateField(blank=True, null=True)
	tags=fields.ArrayField(models.CharField(max_length=200), blank=True,default=list)
	clicks=models.IntegerField(blank=True,default=0)
	likes=models.IntegerField(blank=True,default=0)
	dislikes=models.IntegerField(blank=True,default=0)
	preferences=fields.JSONField(blank=True,default=dict)
	thumbnail=models.ImageField(upload_to='post_image/%Y.%m',default='defaults/pimg.jpeg')
	slug=models.SlugField(max_length=80,null=True,blank=True)

	objects=models.Manager()
	published=PublishedMenager()
	class Meta:
		ordering=['-published_date']
		indexes=[models.Index(fields=['-published_date']),]

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail',kwargs={'slug':self.slug})

	def get_full_url(self):
	    return settings.WEBSITE_URL+self.get_absolute_url()

	def delete(self,*args,**kwargs):
		self.thumbnail.delete()
		super().delete(*args,**kwargs)

	def make_slug(self,*args,**kwargs):
		self.slug=slugify(self.title[:50])+slugify(timezone.now())


class Comment(models.Model):
	post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	author=models.ForeignKey(ProfileInfo,on_delete=models.SET_NULL,
		related_name='comments',null=True)
	text=models.CharField(max_length=250)
	date_added=models.DateField(blank=True,default=timezone.now())




