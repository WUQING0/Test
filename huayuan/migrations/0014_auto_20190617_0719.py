# Generated by Django 2.1.8 on 2019-06-16 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huayuan', '0013_delete_ardiunodata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='personal_information',
        ),
        migrations.DeleteModel(
            name='pipei',
        ),
        migrations.DeleteModel(
            name='userRegister',
        ),
    ]