# Generated by Django 4.0.1 on 2022-01-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_answer_answertext_answer_questiontext'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='res1',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='res2',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='res3',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='res4',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='res5',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='res6',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='res7',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]
