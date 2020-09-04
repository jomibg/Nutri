from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
from .models import ProfileInfo
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import PermissionDenied
from blog.models import Comment

@receiver(post_save,sender=User)
def create_info(sender,instance,created,**kwargs):
	if created:
		ProfileInfo.objects.create(user=instance)
		print('created')
	else:
		instance.info.save()
		print("acitivty updated")

@receiver(pre_save,sender=Comment)
def comment_pre(sender,instance,**kwargs):
	if instance.author.last_comment != date.today():
		instance.author.last_comment=date.today()
		instance.author.comments_per_day=0
	elif not (instance.author.comments_per_day <= 10 or instance.author.user.is_superuser):
		raise PermissionDenied()

@receiver(post_save,sender=Comment)
def comment_added(sender,instance,created,**kwargs):
	if created:
		instance.author.comments_per_day+=1
		instance.author.save()

@receiver(pre_delete,sender=Comment)
def comment_removed(sender,instance,**kwargs):
	if instance.date_added == date.today():
		instance.author.comments_per_day-=1
		instance.author.save()