# Generated by Django 4.0.1 on 2022-02-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_quiz_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_parent',
            field=models.BooleanField(default=False, verbose_name='Родитель'),
        ),
    ]
