from django import forms
from .models import Subscription

class SubForm(forms.ModelForm):
	class Meta:
		model=Subscription
		fields=['weekly']
		labels={'weekly':'Obaveštenja na nedeljnom nivou:',}

