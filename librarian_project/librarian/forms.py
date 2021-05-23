from django import forms
from librarian.models import Author, Book, Profile, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'content']

