# Generated by Django 4.0.1 on 2022-01-30 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_quiz_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='useranswers',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswers',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответ'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
        migrations.AddField(
            model_name='answer',
            name='answerId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='questionId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api.quiz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='age',
            field=models.IntegerField(default=1, max_length=200, verbose_name='Год'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='country',
            field=models.CharField(default=1, max_length=200, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='email',
            field=models.CharField(default=1, max_length=500, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='first_name',
            field=models.CharField(default=1, max_length=500, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='last_name',
            field=models.CharField(default=1, max_length=500, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='phone',
            field=models.CharField(default=1, max_length=50, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='UserAnswers',
        ),
    ]
