from dal import autocomplete

from django import forms

from librarian.models import Author, Book


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=autocomplete.ModelSelect2(url='author-autocomplete')
    )

    class Meta:
        model = Book
        fields = ('__all__')
