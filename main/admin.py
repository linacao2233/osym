from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Exam)
admin.site.register(QuestionInstruction)
admin.site.register(QuestionParagaraph)
admin.site.register(Sentence)
admin.site.register(AnswerSelection)