from django.contrib import admin
from .models import *
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Quiz)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'age', 'country']
    inlines = [AnswerInline]
