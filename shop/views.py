import math

from django.shortcuts import render, get_object_or_404
from .models import Edition
from django.core.paginator import Paginator


# Create your views here.

def edition_list(request):
    editions = Edition.objects.all()

    context = {
        'editions': editions,
    }
    return render(request, 'shop/edition/list.html', context)

# Пока не пригодился
def edition_list_paginator(request):
    editions = Edition.objects.all()
    paginator = Paginator(editions, 4)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {
        'page': page,
        'editions': page.object_list,
    }
    return render(request, 'shop/edition/list_paginator.html', context)


def edition_detail(request, id, slug):
    edition = get_object_or_404(Edition, id=id, slug=slug)
    context = {
        'edition': edition
    }
    return render(request, 'shop/edition/detail.html', context)

# Формирую наборы по 4 книги, пытался их прокручвать
def slides_4(request):
    editions = Edition.objects.all()

    # Количество книг
    count = len(editions)

    set_book = []
    slide = []
    page = 1

    for book in editions:
        slide.append(book)
        # Если последний элемент в списке - добавить слайд на витрину
        if page == count:
            set_book.append(slide)
        # Если 4 элемента уже добавлено в слайд, то наполняю новый слайд
        if len(slide) > 3:
            set_book.append(slide)
            slide = []
        page = page + 1

    count_set_book = len(set_book)

    context = {
        'editions': editions,
        'count_set_book': count_set_book,
        'set_book': set_book,
    }
    return render(request, 'shop/edition/slides_4.html', context)
