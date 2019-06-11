from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'question' 

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    fields = ['question', 'first']
    list_display = ['question', 'first']


admin.site.register(Question, QuestionAdmin)

