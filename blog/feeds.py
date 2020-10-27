from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html,striptags
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
	title="NutriBlog"
	link=reverse_lazy('blog:post_display')
	description="New posts of my blog"
	language="sr"

	def items(self):
		return Post.published.all()[:5]

	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return striptags(truncatewords_html(item.text,30))
	
