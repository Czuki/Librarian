from django.shortcuts import render, redirect
from django.views import View
from librarian.models import Author, Book



class HomeView(View):
    def get(self, request):
        context = {
            'authors': Author.objects.all(),
            'books': Book.objects.all(),
            'recent_books': Book.objects.order_by('-id')[:5],
                   }
        return render(request, 'librarian/__base__.html', context)

    def post(self, request):
        new_book_title = request.POST.get('title')
        new_book_author_pk = request.POST.get('author')
        new_book_isbn = request.POST.get('isbn')
        new_book_author = Author.objects.get(pk=new_book_author_pk)
        # print(new_book_title, type(new_book_author), new_book_isbn)

        if all([new_book_title, new_book_author_pk, new_book_isbn]):
            new_book = Book()
            new_book.name = new_book_title
            new_book.author = Author.objects.get(pk=new_book_author_pk)
            new_book.isbn = new_book_isbn
            new_book.save()

        return redirect('/')


class AuthorAdd(View):

    def get(self, request):
        context = {
            'authors': Author.objects.all(),
            'books': Book.objects.all(),
            'recent_books': Book.objects.order_by('-id')[:5],
                   }
        return render(request, 'librarian/add-author.html', context)












