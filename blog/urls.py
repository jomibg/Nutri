app_name='blog'
from django.urls import path
from .views import *
from .feeds import LatestPostsFeed

urlpatterns = [
path('topics/',TopicsList.as_view(),name='topic_list'),
path('topic/<int:pk>',TopicDetail.as_view(),name='topic_detail'),
path('topic/create',TopicCreate.as_view(),name='topic_create'),
path('topic/<int:pk>/delete',delete_topic,name='topic_delete'),
path('post/add',PostCreate.as_view(),name='post_create'),
path('post/display',UserPostsDisplay.as_view(),name='post_display'),
path('post/unpublished',UnpublishedPostsDisplay.as_view(),name='post_unpublished'),
path('post/<slug:slug>',PostDetail.as_view(),name='post_detail'),
path('comment/<slug:slug>',add_comment,name='comment_add'),
path('comments/<slug:slug>',comment_list,name='comment_list'),
path('comment/remove/<int:pk>',comment_remove,name='comment_delete'),
path('post/publish/<int:pk>',publish,name='post_publish'),
path('post/update/<slug:slug>',UpdatePost.as_view(),name='post_update'),
path('post/delete/<int:pk>',PostDelete.as_view(),name='post_delete'),
path('preference/<int:pk>/<slug:value>',add_pref,name='preference_add'),
path('feed/',LatestPostsFeed(),name='posts_feed')
] 