# Generated by Django 4.0.1 on 2022-01-29 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_useranswers_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='owner',
        ),
    ]
