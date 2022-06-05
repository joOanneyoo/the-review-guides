from django.shortcuts import render, redirect
from django .http import HttpResponse
from account.models import Account
from .models import Booklist, UserQuestion, UserAnswer, BookReview



def home_screen_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    user_questions = UserQuestion.objects.all()

    if request.method == "POST":
        questions = UserQuestion()
        questions.username = request.user.username
        questions.question = request.POST.get('question')
        questions.save()

    return render(request, "thereviewguides/home.html", {'user_questions': user_questions})


def books(request):
    romance = Booklist.objects.filter(genre_type__type="Romance")
    comedy = Booklist.objects.filter(genre_type__type="Comedy")
    horror = Booklist.objects.filter(genre_type__type="Horror")
    fantasy = Booklist.objects.filter(genre_type__type="Fantasy")
    return render(request, 'thereviewguides/books.html', {'romance': romance, 'comedy': comedy, 'horror': horror, 'fantasy': fantasy})


def book_temp(request, id):
    books = Booklist.objects.get(id=id)
    review = BookReview.objects.all()

    if request.method == "POST":
        rev = BookReview()
        rev.book_title = books
        rev.username = request.user.username
        rev.comment = request.POST.get('comment')
        rev.rating = request.POST.get('rating')
        rev.save()

    return render(request, 'thereviewguides/eachBook.html', {'books': books, 'review': review})


def question_temp(request, id):
    questions_list = UserQuestion.objects.get(id=id)
    answer_list = UserAnswer.objects.all()
    answers =UserAnswer()

    if request.method == "POST":
        answers.question = questions_list
        answers.answer = request.POST.get('answer')
        answers.username = questions_list.username
        answers.save()

    return render(request, 'thereviewguides/questions.html', {'questions_list': questions_list, 'answer_list': answer_list})


def destroyReview(request, id):
    review = BookReview.objects.get(id=id)
    review.delete()
    return redirect('/')


def destroyQuestion(request, id):
    answer_list = UserAnswer.objects.get(id=id)
    answer_list.delete()
    return redirect('/')


