from django.contrib import admin
from django.urls import path, include
from librarian.views import (
    IndexView,
    BookAdd,
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
    ReviewAdd,
    ReviewDetails,
)


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('add-book/', BookAdd.as_view(), name='add-book'),
    path('list-books/', BookList.as_view(), name='list-books'),
    path('delete-book/<int:book_id>/', BookDelete.as_view(), name='delete-book'),
    path('add-author/', AuthorAdd.as_view(), name='add-author'),
    path('list-authors/', AuthorList.as_view(), name='list-authors'),
    path('delete-author/<int:author_id>/', AuthorDelete.as_view(), name='delete-author'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('fav-book/<int:book_id>/', FavBook.as_view(), name='fav-book'),
    path('fav-book-remove/<int:book_id>/', FavBookRemove.as_view(), name='fav-book-remove'),
    path('reviews/', ReviewsView.as_view(), name='reviews'),
    path('reviews/add/', ReviewAdd.as_view(), name='add-review'),
    path('reviews/<int:review_id>/', ReviewDetails.as_view(), name='details-review'),
]
