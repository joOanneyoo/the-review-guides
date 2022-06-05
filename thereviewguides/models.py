from django.db import models


class Genre(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Booklist(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=50)
    yearReleased = models.IntegerField()
    genre_type = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='Booklist')
    description = models.CharField(max_length=10000)
    img_url = models.CharField(max_length=3000)

    def __str__(self):
        return self.title
        return self.genre_type.type


class UserQuestion(models.Model):
    username = models.CharField(max_length=30)
    question = models.CharField(max_length=5000)


class UserAnswer(models.Model):
    question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE, related_name='UserAnswer')
    answer = models.CharField(max_length=5000)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.question.question


class UserAnswers(models.Model):
    question = models.CharField(max_length=5000)
    answer = models.CharField(max_length=5000)


class UserAnswer_list(models.Model):
    question = models.CharField(max_length=5000)
    answer = models.CharField(max_length=5000)
    username = models.CharField(max_length=30)


class BookReview(models.Model):
    book_title = models.ForeignKey(Booklist, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    comment = models.TextField(max_length=2000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.book_title.title



