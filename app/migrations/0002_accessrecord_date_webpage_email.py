# Generated by Django 4.2.7 on 2023-12-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='date',
            field=models.DateField(default='2023-12-14'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='india@gmail.com', max_length=254),
        ),
    ]
