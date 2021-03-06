from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #TODO: zmienic na get_user_model()

from librarian.models import Author, Book, Profile, Review
from librarian.forms import ReviewForm

#TODO: ujednolicic jezyk na stronie


def signup(request):
    """User registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'librarian/signup.html', {'form': form})


class IndexView(View):
    """Homepage with site description and list of recently added books"""
    def get(self, request):
        context = {
            'recent_books': Book.objects.order_by('-id')[:5],
        }
        return render(request, 'librarian/index.html', context)


class BookAdd(View):
    """View for adding new books"""
    def get(self, request):
        context = {
            'authors': Author.objects.all().order_by('author'),
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


class BookDetails(View):
    """Shows details about a book, its author and reviews"""
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        reviews_count = Review.objects.filter(book=book).count()
        context = {
            'book': book,
            'reviews_count': reviews_count,
        }
        return render(request, 'librarian/details-book.html', context)


class BookList(View):
    """List of all books with pagination"""
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


class BookDelete(View):
    """Removes book from database, only for admins"""
    def get(self, request, book_id):
        if self.request.user.has_perm('librarian.delete_book'):
            book_to_delete = get_object_or_404(Book, pk=book_id)
            book_to_delete.delete()
            return redirect('/list-books/')
        else:
            return render(request, 'librarian/list-books.html', {'message': 'Nie masz dost??pu do tej akcji'})


class AuthorAdd(View):
    """Adds new author to database"""
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
        full_name = first_name + ' ' + last_name
        Author.objects.create(
            author=full_name
        )
        return redirect('/add-author/')


class AuthorList(View):
    """Lists all authors with pagination """
    def get(self, request):
        authors_list = Author.objects.all().order_by('author')
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


class AuthorDetails(View):
    """Shows author details, with """
    def get(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        author_books = Book.objects.filter(author=author)
        context = {
            'author': author,
            'books': author_books,
        }
        return render(request, 'librarian/details-author.html', context)


class AuthorDelete(View):
    """Remove Author from database"""
    def get(self, request, author_id):
        if self.request.user.has_perm('librarian.delete_author'):
            author_to_delete = get_object_or_404(Author, pk=author_id)
            author_to_delete.delete()
            return redirect('/list-authors/')
        else:
            return render(request, 'librarian/list-authors.html', {'message': 'Nie masz dost??pu do tej akcji'})


class ProfileView(View):
    """Shows user profile"""
    def get(self, request):
        current_user = get_object_or_404(User, pk=request.user.id)
        prof = Profile.objects.get(user=current_user)
        context = {
            'current_user': prof,
            'fav_books': prof.fav_books.all(),
            'fav_authors': prof.fav_authors.all(),
        }
        return render(request, 'librarian/profile.html', context)


class FavAuthor(View):
    """Adds Author to favorites"""
    def get(self, request, author_id):
        current_user = get_object_or_404(User, pk=request.user.id)
        profile = Profile.objects.get(user=current_user)
        fav_authors = profile.fav_authors.all()
        liked_author = get_object_or_404(Author, pk=author_id)
        if liked_author not in fav_authors:
            profile.fav_authors.add(liked_author)
            return redirect('/profile/')
        return redirect('/list-authors/')


class FavAuthorRemove(View):
    """Removes author from favorites"""
    def get(self, request, author_id):
        current_user = get_object_or_404(User, pk=request.user.id)
        profile = Profile.objects.get(user=current_user)
        unliked_author = get_object_or_404(Author, pk=author_id)
        profile.fav_authors.remove(unliked_author)
        return redirect('/profile/')


class FavBook(View):
    """Adds book to favorites"""
    def get(self, request, book_id):
        current_user = get_object_or_404(User, pk=request.user.id)
        profile = Profile.objects.get(user=current_user)
        fav_books = profile.fav_books.all()
        liked_book = get_object_or_404(Book, pk=book_id)
        if liked_book not in fav_books:
            profile.fav_books.add(liked_book)
            return redirect('/profile/')
        return redirect('/list-books/')


class FavBookRemove(View):
    """Removes book from favorites"""
    def get(self, request, book_id):
        current_user = get_object_or_404(User, pk=request.user.id)
        profile = Profile.objects.get(user=current_user)
        unliked_book = get_object_or_404(Book, pk=book_id)
        profile.fav_books.remove(unliked_book)
        return redirect('/profile/')


class ReviewsView(View):
    """Shows all book reviews"""
    def get(self, request):
        book_reviews = Review.objects.all()
        context = {
            'book_reviews': book_reviews,
        }
        #TODO: add review buttons for books
        return render(request, 'librarian/reviews.html', context)


class ReviewAdd(View):
    """Shows review form for writing new book review"""
    def get(self, request):
        form = ReviewForm()
        context = {
            'form': form,
        }
        return render(request, 'librarian/add-review.html', context)

    def post(self, request):
        form = ReviewForm(request.POST)
        if self.request.user.is_authenticated:
            current_user = get_object_or_404(User, pk=request.user.id)
            if form.is_valid():
                Review.objects.create(
                    book=form.cleaned_data['book'],
                    content=form.cleaned_data['content'],
                    reviewer=current_user,
                )
        return redirect('/reviews/')


class ReviewDetails(View):
    """Shows full review with details"""
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        context = {
            'review': review,
        }
        return render(request, 'librarian/details-review.html', context)
