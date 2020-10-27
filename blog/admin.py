from django.contrib import admin
from django.forms.widgets import CheckboxSelectMultiple
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	formfield_overrides={
	models.ManyToManyField:{'widget':CheckboxSelectMultiple}
	}
admin.site.register(Topic)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
