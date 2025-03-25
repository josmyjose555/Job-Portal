# Generated by Django 4.0.6 on 2022-09-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer_app', '0002_joblist'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='mobile',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
