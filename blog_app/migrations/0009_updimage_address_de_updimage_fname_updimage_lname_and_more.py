# Generated by Django 4.1.5 on 2023-03-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_updimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='updimage',
            name='address_de',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='updimage',
            name='fname',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='updimage',
            name='lname',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='updimage',
            name='phone_no',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
