# Generated by Django 4.1.5 on 2023-03-16 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_proimage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proimage',
            name='name',
        ),
    ]