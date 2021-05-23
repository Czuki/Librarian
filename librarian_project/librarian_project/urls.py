from django.contrib import admin
from django.urls import path, include
import librarian.views as lib_views


urlpatterns = [
    path('signup/', lib_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    #TODO: reszta widokow z auth.urls
    path('admin/', admin.site.urls),
    path('', lib_views.IndexView.as_view(), name='index'),

    path('add-book/', lib_views.BookAdd.as_view(), name='add-book'),
    path('list-books/', lib_views.BookList.as_view(), name='list-books'),
    path('delete-book/<int:book_id>/', lib_views.BookDelete.as_view(), name='delete-book'),
    path('book/<int:book_id>/', lib_views.BookDetails.as_view(), name='details-book'),

    path('add-author/', lib_views.AuthorAdd.as_view(), name='add-author'),
    path('list-authors/', lib_views.AuthorList.as_view(), name='list-authors'),
    path('delete-author/<int:author_id>/', lib_views.AuthorDelete.as_view(), name='delete-author'),
    path('author/<int:author_id>/', lib_views.AuthorDetails.as_view(), name='details-author'),

    path('profile/', lib_views.ProfileView.as_view(), name='profile'),

    path('fav-book/<int:book_id>/', lib_views.FavBook.as_view(), name='fav-book'),
    path('fav-book-remove/<int:book_id>/', lib_views.FavBookRemove.as_view(), name='fav-book-remove'),

    path('fav-author/<int:author_id>/', lib_views.FavAuthor.as_view(), name='fav-author'),
    path('fav-author-remove/<int:author_id>/', lib_views.FavAuthorRemove.as_view(), name='fav-author-remove'),


    path('reviews/', lib_views.ReviewsView.as_view(), name='reviews'),
    path('reviews/add/', lib_views.ReviewAdd.as_view(), name='add-review'),
    # path('reviews/add', lib_views.ReviewAdd.as_view(), name='add-review'),
    path('reviews/<int:review_id>/', lib_views.ReviewDetails.as_view(), name='details-review'),
]
