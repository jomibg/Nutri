from django.db.models import Avg,Q,F,Case,When,Exists,Value
from .models import *
from django.utils import timezone

def most_viewed_posts():
	rating=Post.published.aggregate(average=Case(
		When(Exists(Post.published.all()),then=Avg('clicks')),
		default=Value(0),
		))
	posts=Post.published.filter(clicks__gt=rating['average'])[:5]
	return posts
	
def post_search(key):
	posts=Post.published.filter(
		Q(title__icontains=key) | Q(tags__overlap=key.split()) | Q(tags__overlap=key.split(',')))[:10]
	return posts
###########################za produkciju/sitemap#########################################
'''def last_mod_date(tkey):
	post=Post.published(topic=tkey)[0]
	return post.published_date'''