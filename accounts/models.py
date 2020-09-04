from django.db import models
from array import array
# Create your models here.
class ProfileInfo(models.Model):
	user=models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name='info')
	last_comment=models.DateField(blank=True,null=True)
	comments_per_day=models.IntegerField(blank=True,default=0)
	
	def __str__(self):
		return str(self.user)