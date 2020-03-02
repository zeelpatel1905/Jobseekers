import os
import random
from django.db.models.signals import pre_save, post_save
from django.db import models
from django.forms import forms
from Home.models import *


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = instance.name + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "company/{final_filename}".format(final_filename=final_filename)



class Dept(models.Model):
    dept_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return  self.dept_name

class Designation(models.Model):
    Designation_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Designation_name

class Company_service(models.Model):
    service_name  = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return  self.service_name

class Company(models.Model):
    company_id = models.CharField(max_length=50, null=True, blank=True)
    company_register_number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=30)
    company_phone = models.CharField(max_length=10)
    company_fax_number = models.CharField(max_length=20)
    company_category = models.CharField(max_length=50)
    company_services = models.ManyToManyField(Company_service)
    company_total_emp_no = models.IntegerField()
    company_total_dept = models.IntegerField()
    company_desc = models.TextField()
    company_logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    company_street_name = models.CharField(max_length=50)
    company_city = models.ManyToManyField(City)
    company_states = models.ManyToManyField(States)
    company_country = models.CharField(default='India', max_length=10, editable=False)
    company_pincode = models.IntegerField()
    company_website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

def company_id_pre_save_receiver(sender, instance, *args, **kwargs):
    a = random.randint(1,5)
    instance.company_id = instance.name + "@" + str(a)

pre_save.connect(company_id_pre_save_receiver, sender=Company)


class Employee(models.Model):
    Gender = (
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other"),
    )

    emp_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emp_dept = models.ManyToManyField(Dept)
    emp_designation = models.ManyToManyField(Designation)
    name = models.CharField(max_length=40)
    emp_last_name = models.CharField(max_length=40)
    emp_email = models.EmailField(max_length=30)
    emp_phone = models.CharField(max_length=10)
    emp_password = models.CharField(max_length=50, null=True, blank=True)
    emp_bio = models.TextField(blank=True, null=True)
    emp_birthdate = models.DateField(null=True, blank=True)
    emp_gender = models.CharField(max_length=1,choices=Gender)
    emp_id_card = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    emp_experience = models.DecimalField(decimal_places=2,max_digits=4)
    emp_street_name = models.CharField(max_length=50)
    emp_city = models.ForeignKey(City, on_delete=models.CASCADE)
    emp_states = models.ForeignKey(States, on_delete=models.CASCADE)
    emp_country = models.CharField(default='India', max_length=10, editable=False)
    emp_pincode = models.IntegerField()
    is_super_emp = models.BooleanField(default=0)


    def __str__(self):
        return  self.name

def password_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.emp_password = instance.name + "@" + str(instance.emp_birthdate)

pre_save.connect(password_pre_save_receiver, sender=Employee)

class Job_upload(models.Model):
    comapny_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=30)
    job_description = models.TextField(blank=True, null=True)
    job_salary = models.DecimalField(decimal_places=2, max_digits=8)
    job_street_name = models.CharField(max_length=50)
    job_city = models.ForeignKey(City, on_delete=models.CASCADE)
    job_states = models.ForeignKey(States, on_delete=models.CASCADE)
    job_country = models.CharField(default='India', max_length=10, editable=False)
    job_qualification = models.CharField(max_length=30)
    job_quentity = models.IntegerField()
    job_upload_date = models.DateTimeField(auto_now_add=True)
    job_deadline = models.DateField()
    job_bond_time = models.IntegerField()
    job_bond_documents = models.TextField(max_length=40)

    def __str__(self):
        return self.job_title

