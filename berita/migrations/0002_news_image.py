# Generated by Django 2.2 on 2020-12-15 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
