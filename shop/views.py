from django.shortcuts import render, get_object_or_404
from .models import Edition


# Create your views here.

def edition_list(request):
    editions = Edition.objects.all()

    context = {
        'editions': editions,
    }
    return render(request, 'shop/edition/list.html', context)


def edition_detail(request, id, slug):
    edition = get_object_or_404(Edition, id=id, slug=slug)
    context = {
        'edition': edition
    }
    return render(request, 'shop/edition/detail.html', context)
