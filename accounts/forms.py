from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django_registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User
class FormaPrijava(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(FormaPrijava,self).__init__(*args,**kwargs)
	username=forms.CharField(required=True,label='Korisničko ime:',widget=forms.TextInput(attrs={'class':'auth-input',}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Šifra:')
class FormaPromena(PasswordChangeForm):
	def __init__(self,*args,**kwargs):
		super(FormaPromena,self).__init__(*args,**kwargs)
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Nova šifra:')
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Potvrdi šifru:')
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Stara šifra:')
class FormaIzmena(SetPasswordForm):
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Nova šifra:')
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Potvrdi šifru:')
class FormaRegistracija(RegistrationFormUniqueEmail):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Unesite šifru:')
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'auth-input',}),label='Ponovite šifru:')
	username=forms.CharField(required=True,label='Korisničko ime:',widget=forms.TextInput(attrs={'class':'auth-input',}))
	email=forms.EmailField(required=True,label='Email:',widget=forms.EmailInput(attrs={'class':'auth-input',}))
	
class IzmeniProfil(forms.ModelForm):
	username=forms.CharField(required=True,label='Korisničko ime:',widget=forms.TextInput(attrs={'class':'auth-input',}))
	email=forms.EmailField(required=True,label='Email:',widget=forms.EmailInput(attrs={'class':'auth-input',}))
	class Meta:
		model=User
		fields=['username','email']