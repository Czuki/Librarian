from django.contrib import admin
from django.urls import path, include
from librarian.views import HomeView, AuthorAdd, AuthorDelete, AuthorList, BookList, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('add-book/', HomeView.as_view(), name='add-book'),
    path('list-books/', BookList.as_view(), name='list-books'),
    path('add-author/', AuthorAdd.as_view(), name='add-author'),
    path('list-authors/', AuthorList.as_view(), name='list-authors'),
    path('delete-author/<int:author_id>/', AuthorDelete.as_view(), name='delete-author'),
]
