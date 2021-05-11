from django.db import models
from django.urls import reverse


# Create your models here.
class Language(models.Model):
    nameLanguage = models.CharField(max_length=20, verbose_name='Язык')

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.nameLanguage


class Genre(models.Model):
    nameGenre = models.CharField(max_length=100, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.nameGenre


class Book(models.Model):
    genre = models.ForeignKey(Genre,
                              related_name='books',
                              on_delete=models.CASCADE,
                              verbose_name='Жанр')
    nameBook = models.CharField(max_length=200, verbose_name='Название книги')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.nameBook


class Edition(models.Model):
    book = models.ForeignKey(Book,
                             related_name='editions',
                             on_delete=models.CASCADE,
                             verbose_name='Название книги')
    language = models.ForeignKey(Language,
                                 related_name='editions',
                                 on_delete=models.CASCADE,
                                 verbose_name='Язык')
    slug = models.SlugField(max_length=200, verbose_name='url',  unique=True)
    weight = models.IntegerField(blank=True, default=140, verbose_name='Вес')
    height = models.IntegerField(blank=True, default=30, verbose_name='Высота')
    width = models.IntegerField(blank=True, default=20, verbose_name='Ширина')
    numberOfPages = models.IntegerField(blank=True, default=170, verbose_name='Количество страниц')
    yearOfIssue = models.IntegerField(blank=True, default=2021, verbose_name='Год издания')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=55, verbose_name='Цена')
    photo = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.book.nameBook

    def get_absolute_url(self):
        return reverse('shop:edition_detail', args=[self.id, self.slug])
