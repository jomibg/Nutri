from django import forms
from .models import *
from django.contrib.postgres.forms import SimpleArrayField
from froala_editor.widgets import FroalaEditor

class PostCreateForm(forms.ModelForm):
	tags=SimpleArrayField(forms.CharField(),required=False,label='Tagovi')
	class Meta:
		model=Post
		exclude=['published_date','clicks','likes','dislikes','preferences','meta_keywords']
		widgets={
		'text':FroalaEditor(image_upload=True),}
		labels={'title':'Naslov','topic':'Tema'}
class CommentForm(forms.Form):
	text=forms.CharField(max_length=250,min_length=10,
		widget=forms.Textarea(attrs={'rows': '5','style':'width:200px;','placeholder':'Ostavite komentar...'}))

class SearchForm(forms.Form):
	key=forms.CharField(max_length=250,min_length=1,
		widget=forms.TextInput(attrs={'placeholder':'Pretraži objave...'}),
		label='')

class AddImageForm(forms.ModelForm):
	class Meta:
		model=Additional_image
		fields=['image','title']
		labels={'image':'slika','title':'naslov'}


ImagesFormset=forms.inlineformset_factory(Post,Additional_image,fields=('image','title'),labels={'image':'slika','title':'naslov'},max_num=5,extra=3)
