from django import forms
from thereviewguides.models import UserQuestion, BookReview


class UserQuestionForm(forms.ModelForm):
    class Meta:
        model = UserQuestion
        fields = {"username", "question"}


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = {"username", "comment", "rating"}