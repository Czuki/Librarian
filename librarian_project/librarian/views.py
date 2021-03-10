from django.shortcuts import render
from django.views import View
from librarian.models import Author, Book

class HomeView(View):
    def get(self, request):

        context = {
            'authors': Author.objects.all(),
            'books': Book.objects.all(),
                   }
        return render(request, 'librarian/base.html', context)













