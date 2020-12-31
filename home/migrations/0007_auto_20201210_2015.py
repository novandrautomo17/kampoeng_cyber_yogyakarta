# Generated by Django 2.2 on 2020-12-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201210_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='caption_image_1',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='caption_image_2',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='caption_image_3',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='caption_image_4',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image4',
        ),
        migrations.AddField(
            model_name='carousel',
            name='about_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='about_image',
            field=models.ImageField(null=True, upload_to='about_image'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='title_about',
            field=models.CharField(max_length=200, null=True),
        ),
    ]