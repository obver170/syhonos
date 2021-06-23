from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddEditionForm
# from ..shop.models import Edition
from shop.models import Edition



# Create your views here.

@require_POST
def cart_add(request, edition_id):
    cart = Cart(request)
    edition = get_object_or_404(Edition, id=edition_id)
    form = CartAddEditionForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(edition=edition, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, edition_id):
    cart = Cart(request)
    edition = get_object_or_404(Edition, id=edition_id)
    cart.remove(edition)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
