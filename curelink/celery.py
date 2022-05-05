from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from django.core.mail import send_mass_mail
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curelink.settings')
app = Celery('curelink')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def send_email_to_reciepent(content, content_desc, reciepents):
    print(content, content_desc,reciepents)
    send_mass_mail(content_desc,content,'Curelink Newsletter <'+settings.EMAIL_HOST_USER+'>', reciepents, fail_silently=True)
    return "Done "
    