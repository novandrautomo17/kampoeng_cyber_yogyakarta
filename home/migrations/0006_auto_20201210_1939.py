# Generated by Django 2.2 on 2020-12-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201210_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image1',
            field=models.ImageField(upload_to='carousel'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image2',
            field=models.ImageField(upload_to='carousel'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image3',
            field=models.ImageField(upload_to='carousel'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image4',
            field=models.ImageField(upload_to='carousel'),
        ),
    ]
