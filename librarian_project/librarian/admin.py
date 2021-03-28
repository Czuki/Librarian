from django.contrib import admin
from librarian.models import Author, Book, Profile


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Book, BookAdmin)

