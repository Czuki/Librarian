from django.contrib import admin
from librarian.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)


admin.site.register(Book, BookAdmin)

