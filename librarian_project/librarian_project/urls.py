from django.contrib import admin
from django.urls import path, include
from librarian.views import (
    HomeView,
    AuthorAdd,
    AuthorDelete,
    AuthorList,
    BookList,
    BookDelete,
    signup,
    ProfileView,
    FavBook,
    FavBookRemove,
    ReviewsView,
)


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('add-book/', HomeView.as_view(), name='add-book'),
    path('list-books/', BookList.as_view(), name='list-books'),
    path('delete-book/<int:book_id>/', BookDelete.as_view(), name='delete-book'),
    path('add-author/', AuthorAdd.as_view(), name='add-author'),
    path('list-authors/', AuthorList.as_view(), name='list-authors'),
    path('delete-author/<int:author_id>/', AuthorDelete.as_view(), name='delete-author'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('fav-book/<int:book_id>/', FavBook.as_view(), name='fav-book'),
    path('fav-book-remove/<int:book_id>/', FavBookRemove.as_view(), name='fav-book-remove'),
    path('reviews/', ReviewsView.as_view(), name='reviews'),
]
