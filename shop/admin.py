from django.contrib import admin
from .models import Language, Genre, Book, Edition


# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['nameLanguage']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['nameGenre']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['genre', 'nameBook', 'description']


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ['book', 'language', 'weight', 'height', 'width', 'numberOfPages', 'yearOfIssue', 'price']
    list_editable = ['language', 'weight', 'height', 'width', 'numberOfPages', 'yearOfIssue', 'price']

