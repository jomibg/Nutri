from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django_registration.forms import RegistrationFormUniqueEmail
class FormaPrijava(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(FormaPrijava,self).__init__(*args,**kwargs)
	username=forms.CharField(required=True,label='Korisničko ime:')
	password = forms.CharField(widget=forms.PasswordInput(),label='Šifra:')
class FormaPromena(PasswordChangeForm):
	def __init__(self,*args,**kwargs):
		super(FormaPromena,self).__init__(*args,**kwargs)
	new_password1=forms.CharField(widget=forms.PasswordInput(),label='Nova šifra:')
	new_password2=forms.CharField(widget=forms.PasswordInput(),label='Potvrdi šifru:')
	old_password=forms.CharField(widget=forms.PasswordInput(),label='Stara šifra:')
class FormaIzmena(SetPasswordForm):
	new_password1=forms.CharField(widget=forms.PasswordInput(),label='Nova šifra:')
	new_password2=forms.CharField(widget=forms.PasswordInput(),label='Potvrdi šifru:')
class FormaRegistracija(RegistrationFormUniqueEmail):
	password1=forms.CharField(widget=forms.PasswordInput(),label='Unesite šifru:')
	password2=forms.CharField(widget=forms.PasswordInput(),label='Ponovite šifru:')
	class Meta(RegistrationFormUniqueEmail.Meta):
		labels={'username':'Korisničko ime:','email':'Email:'}
