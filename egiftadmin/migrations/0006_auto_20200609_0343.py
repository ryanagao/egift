# Generated by Django 2.1.15 on 2020-06-09 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egiftadmin', '0005_auto_20200531_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='about',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='accountrequest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='accountrequest',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='branches',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='branches',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
    ]
