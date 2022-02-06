from django.db import models

# Create your models here.



class Quiz(models.Model):
    first_name = models.CharField("Имя", max_length=500)
    last_name = models.CharField("Фамилия", max_length=500)
    phone = models.CharField("Телефон", max_length=50)
    email = models.CharField("Почта", max_length=500)
    age = models.IntegerField("Год", max_length=200)
    country = models.CharField("Страна", max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    res1 = models.CharField("Ценностно-смысловая организация личности", max_length=255)
    res2 = models.CharField("Организация деятельности", max_length=255)
    res3 = models.CharField("Решительность", max_length=255)
    res4 = models.CharField("Настойчивость", max_length=255)
    res5 = models.CharField("Самообладание", max_length=255)
    res6 = models.CharField("Самостоятельность", max_length=255)
    res7 = models.CharField("Показатель лжи", max_length=255)

    is_parent = models.BooleanField("Родитель", default=False)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.last_name +" " + self.first_name


class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='answers')
    questionId = models.IntegerField()
    answerId = models.IntegerField()
    questionText = models.CharField(max_length=1200)
    answerText = models.CharField(max_length=1200)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответ"

class Code(models.Model):
    code = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Код"
        verbose_name_plural = "Коды"


