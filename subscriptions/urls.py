from django.urls import path
app_name='subscriptions'
from .views import SubscribeView,unsubscribe


urlpatterns=[
path('subscribe/',SubscribeView.as_view(),name='subscribe') ,
path('unsubscribe/',unsubscribe,name='unsubscribe'), 
]
