"""NutritionBLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from django.urls import include
from blog.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views
from blog.sitemaps import *
from django.contrib.sitemaps import views
sitemaps={'posts':PostSiteMap,'topics':TopicSiteMap,'about':AboutSiteMap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('froala_editor/',include('froala_editor.urls')),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('subs/',include('subscriptions.urls')),
    ]
    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/',include(debug_toolbar.urls))]

