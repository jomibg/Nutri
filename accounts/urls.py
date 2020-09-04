from django.urls import path,include 
app_name='accounts' 
from django.contrib.auth import views as av
from django.urls import reverse_lazy 
from .decorators import *
from .views import *
from django_registration.backends.activation.views import RegistrationView,ActivationView
from django.views.generic import TemplateView
from .forms import *
urlpatterns = [
path('login/',redirect_authenticated(av.LoginView.as_view(authentication_form=FormaPrijava))
	,name='login'),
path('logout/',av.LogoutView.as_view(next_page='/'),name='logout'),
path('password_reset/',av.PasswordResetView.as_view(
	success_url=reverse_lazy('accounts:reset_done')),
name='password_reset'),
path('reset/done/',av.PasswordResetDoneView.as_view(),name='reset_done'),
path('reset/<uidb64>/<token>/',av.PasswordResetConfirmView.as_view(
	success_url=reverse_lazy('accounts:reset_complete'),form_class=FormaIzmena),name='reset_confirm'),
path('reset/complete/',av.PasswordResetCompleteView.as_view(),name='reset_complete'),
path('change_info/<int:pk>/',ProfileUpdate.as_view(success_url=reverse_lazy('home')),name='ch_info'),
path('change_password/',av.PasswordChangeView.as_view(success_url=reverse_lazy('home'),form_class=FormaPromena),name='password_change'),
###########Registration################################
path('register/',
redirect_authenticated(RegistrationView.as_view(
	form_class=FormaRegistracija,
	success_url=reverse_lazy('accounts:successfull'),
	disallowed_url=reverse_lazy('accounts:disallowed'))),
name='register'),
path('disallowed/',TemplateView.as_view(template_name='django_registration/disallowed.html'),
	name='disallowed'),
path('successfull/',TemplateView.as_view(template_name='django_registration/successfull.html'),
	name='successfull'),
path("activate/<str:activation_key>/",ActivationView.as_view(success_url=reverse_lazy('accounts:complete')),
	name="django_registration_activate"),
path('activate/complete',TemplateView.as_view(template_name='django_registration/complete.html'),name='complete')
] 

