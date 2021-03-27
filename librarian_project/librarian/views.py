from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from librarian.models import Author, Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'librarian/signup.html', {'form': form})


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
        Book.objects.create(
            name=new_book_title,
            author=Author.objects.get(pk=new_book_author_pk),
            isbn=new_book_isbn
        )
        return redirect('/')


class BookList(View):
    def get(self, request):
        books_list = Book.objects.all().order_by('name')
        paginator = Paginator(books_list, 6)
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context = {
            'page': page,
            'books': books,
        }
        return render(request, 'librarian/list-books.html', context)


class AuthorAdd(View):
    def get(self, request):
        context = {
            'authors': Author.objects.all(),
            'books': Book.objects.all(),
            'recent_books': Book.objects.order_by('-id')[:5],
                   }
        return render(request, 'librarian/add-author.html', context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(
            first_name=first_name,
            last_name=last_name
        )
        return redirect('/add-author/')


class AuthorList(View):
    def get(self, request):
        authors_list = Author.objects.all().order_by('last_name')
        paginator = Paginator(authors_list, 6)
        page = request.GET.get('page')
        try:
            authors = paginator.page(page)
        except PageNotAnInteger:
            authors = paginator.page(1)
        except EmptyPage:
            authors = paginator.page(paginator.num_pages)
        context = {
            'page': page,
            'authors': authors
        }
        return render(request, 'librarian/list-authors.html', context)


class AuthorDelete(View):
    #TODO: only for admins
    def get(self, request, author_id):

        if self.request.user.has_perm('librarian.delete_author'):
            author_to_delete = get_object_or_404(Author, pk=author_id)
            author_to_delete.delete()
            return redirect('/list-authors/')
        else:
            return render(request, 'librarian/list-authors.html', {'message': 'Nie masz dostępu do tej akcji'})
