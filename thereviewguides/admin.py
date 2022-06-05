from django.contrib import admin
from .models import Genre, Booklist, UserQuestion, UserAnswer, BookReview

admin.site.register(Genre)
admin.site.register(Booklist)
admin.site.register(UserQuestion)
admin.site.register(UserAnswer)
admin.site.register(BookReview)