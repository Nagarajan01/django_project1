from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import *


@receiver(post_save, sender=Student_detail)
def create_profile(sender, instance, created, **kwargs):
    if created:
       print("created")
       Mark.objects.create(roll_no=instance)
        

@receiver(post_save, sender=Mark)
def save_profile(sender, instance, **kwargs):
        print('saved')
        ob = Mark.objects.filter(id = 5).values('roll_no__email')
        mylist = ob[0]['roll_no__email']
        instance.roll_no.save()
        send_mail('update', 'your mark is {} updated'.format(instance.mark), 'sendermail@abc.com', [mylist])
