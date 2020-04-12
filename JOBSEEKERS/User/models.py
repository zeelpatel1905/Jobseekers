import os
import random
from django.db.models.signals import pre_save, post_save
from django.db import models
from django.forms import forms
from django.dispatch import receiver
from django.contrib.auth.models import User
from Home.models import *
from django.core.validators import RegexValidator


# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = instance.email + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "user/image/{final_filename}".format(final_filename=final_filename)

def upload_file_path(instance, filename):
    new_filename = instance.email + '_resume' + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "user/resume/{final_filename}".format(final_filename=final_filename)


class Profile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Enter valid phone number must be entered in the format: '+9999999999'.")
    GENDER_CHOICES = (
        ('M', 'Male',),
        ('F', 'Female',),
        ('O', 'Other',),
    )
    EXPRERIENCE_CHOICES = (
        ('E', 'Exprerience'),
        ('F', 'Fresher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, null=True, blank=True)
    contact = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True )
    birth_date = models.DateField(null=True, blank=True)
    skils = models.TextField(max_length=1000, null=True, blank=True)
    resume = models.FileField(upload_to=upload_file_path, null=True, blank=True)
    img = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    exprerience_type = models.CharField(max_length=1, choices=EXPRERIENCE_CHOICES, null=True, blank=True )
    street_name = models.CharField(max_length=50 , null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    states = models.ForeignKey(States, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(default='India', max_length=10, editable=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance , **kwargs):
    instance.profile.save()
