# Generated by Django 2.2 on 2020-12-30 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0005_auto_20201225_0548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tags',
        ),
    ]