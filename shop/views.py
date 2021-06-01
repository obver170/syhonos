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
