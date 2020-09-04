from django.contrib.sitemaps import Sitemap
from .models import Post,Topic
from django.urls import reverse_lazy

class PostSiteMap(Sitemap):
	changefreq = 'yearly'
	priority=0.8

	def items(slef):
		return Post.published.all()

	def lastmod(self,item):
		return item.published_date

class TopicSiteMap(Sitemap):
	changefreq = 'weekly'
	priority=0.6

	def items(slef):
		return Topic.objects.all()



class AboutSiteMap(Sitemap):
	changefreq='never'
	priority=0.4

	def items(self):
		return ['about']

	def location(self,item):
		return reverse_lazy(item)

