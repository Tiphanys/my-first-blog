# Generated by Django 2.1.1 on 2018-09-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180927_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='background',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
