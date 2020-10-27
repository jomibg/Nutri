from celery import shared_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask, IntervalSchedule
from celery.utils.log import get_task_logger
from blog.models import Post
from django.contrib.auth.models import User
from datetime import date,timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models import Avg,Q,Case,When,Exists,Value

logger=get_task_logger(__name__)

@shared_task(bind=True)
def ew_msg(self):
    d=date.today()-timedelta(days=7)
    posts=Post.published.filter(published_date__gte=d)[:5]
    recipients=User.objects.exclude(subscription__weekly__isnull=True)
    html_content=render_to_string('includes/weekly_msg.html',{'posts':posts,'date':date.today().isoformat()})
    txt_content=render_to_string('includes/weekly_msg.txt',{'posts':posts,'date':date.today().isoformat()})
    subject='Objave iz protekle nedelje'
    msg=EmailMultiAlternatives(subject,txt_content,bcc=[u.email for u in recipients])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

@shared_task(bind=True)
def emonthly(self):
	rating=Post.published.aggregate(average=Case(When(Exists(Post.published.all()),then=Avg('clicks')),default=Value(0)))
	d=date.today()-timedelta(days=30)
	posts=Post.published.filter(published_date__gte=d,clicks__gte=rating['average'])[:5]
	recipients=User.objects.exclude(subscription__isnull=True)
	html_content=render_to_string('includes/monthly_msg.html',{'posts':posts,'date':date.today().isoformat()})
	txt_content=render_to_string('includes/monthly_msg.txt',{'posts':posts,'date':date.today().isoformat()})
	subject='Najpopularnije ovog meseca'
	msg=EmailMultiAlternatives(subject,txt_content,bcc=[u.email for u in recipients])
	msg.attach_alternative(html_content,'text/html')
	msg.send()


#schedule_test,created=IntervalSchedule.objects.get_or_create(every=10,period=IntervalSchedule.SECONDS,)
schedule_weekly,_=IntervalSchedule.objects.get_or_create(every=15,period=IntervalSchedule.DAYS)
schedule_monthly,_=IntervalSchedule.objects.get_or_create(every=30,period=IntervalSchedule.DAYS)
#sch_test,_=PeriodicTask.objects.get_or_create(interval=schedule_test,name='Send comercials',task=emonthly.name)
sch_tsk1,_=PeriodicTask.objects.get_or_create(interval=schedule_weekly,name='Send comercial mail/weekly',task=emonthly.name)
sch_tsk1,_=PeriodicTask.objects.get_or_create(interval=schedule_weekly,name='Send comercial mail/monthly',task=ew_msg.name)
