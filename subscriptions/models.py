from django.db import models

# Create your models here.

class Subscription(models.Model):
	user=models.OneToOneField('auth.User',on_delete=models.CASCADE,blank=True,null=True)
	date=models.DateField(auto_now_add=True)
	weekly=models.BooleanField(blank=True,default=False)
	monthly=models.BooleanField(blank=True,default=True)

	def __repr__(self):
		return self.email
