# Generated by Django 4.2.13 on 2024-06-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='e_mail',
            field=models.EmailField(default='kalashchouhan939@gmail.com', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=12345, max_length=6000),
            preserve_default=False,
        ),
    ]
