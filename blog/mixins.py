from django.db import models
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
class MetaTagBase(models.Model):
	meta_keywords = models.CharField(max_length=255,blank=True,)

	class Meta:
		abstract=True

	def get_meta_field(self, name, content):
		tag = ""
		if name and content:
			tag = render_to_string("includes/meta_field.html", {"name": name,"content": content})
			return mark_safe(tag)

	def get_meta_keywords(self):
		return self.get_meta_field("keywords", self.meta_keywords)

class PublishedMenager(models.Manager):
	def get_queryset(self):
		return super(PublishedMenager,self).get_queryset().exclude(published_date__isnull=True)
