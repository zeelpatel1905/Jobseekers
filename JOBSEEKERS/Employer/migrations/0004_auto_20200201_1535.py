# Generated by Django 3.0.2 on 2020-02-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0003_auto_20200113_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]