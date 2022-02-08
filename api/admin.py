from django.contrib import admin
from .models import *
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Quiz)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'age', 'country', 'is_parent']
    inlines = [AnswerInline]

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'id']
