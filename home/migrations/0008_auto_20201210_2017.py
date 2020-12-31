# Generated by Django 2.2 on 2020-12-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201210_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_about', models.CharField(max_length=200, null=True)),
                ('about_desc', models.TextField(null=True)),
                ('about_image', models.ImageField(null=True, upload_to='about_image')),
            ],
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='about_desc',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='about_image',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='title_about',
        ),
        migrations.AddField(
            model_name='carousel',
            name='caption_image_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='caption_image_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='caption_image_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='caption_image_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='image1',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='image2',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='image3',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='image4',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
    ]