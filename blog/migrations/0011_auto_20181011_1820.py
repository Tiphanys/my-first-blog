# Generated by Django 2.1.1 on 2018-10-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181011_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='background',
        ),
        migrations.RemoveField(
            model_name='post',
            name='logo',
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
