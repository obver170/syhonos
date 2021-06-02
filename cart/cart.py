from decimal import Decimal
from django.conf import settings
from ..shop.models import Edition


class Cart(object):

    def __init__(self, request):
        # Инициализация объекта корзины
        self.session = request.sesion
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраниние сессии в пустую корзину
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, edition, quantity=1, update_quantity=False):
        # Добавление товара или обновление количества
        edition_id = str(edition.id)
        if edition_id not in self.cart:
            self.cart[edition_id] = {'quantity': 0, 'price': str(edition.price)}
        if update_quantity:
            self.cart[edition_id]['quantity'] = quantity
        else:
            self.cart[edition_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Пометить сессию завершенной
        self.session.modifed = True

    def remove(self, edition):
        # Удаление товара из корзины
        edition_id = str(edition.id)
        if edition_id in self.cart:
            del self.cart[edition_id]
            self.save()

    def __iter__(self):
        # Пройтись по товарам корзины и получить соответствующие edotion
        edition_ids = self.cart.keys()
        # Получить объекты Edition и передать в корзину
        editions = Edition.objects.filter(id__in=edition_ids)

        cart = self.cart.copy()
        for edition in editions:
            cart[str(edition.id)]['edition'] = edition
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']
            yield item

    def __len__(self):
        # Общее количество товаров в корзине
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # Общая стоимость корзины
        return sum(
            Decimal(item['price'] * item['quantity'])
            for item in self.cart.values()
        )

    def clear(self):
        # Очистка корзины
        del self.session[settings.CART_SESSION_ID]
        self.save()