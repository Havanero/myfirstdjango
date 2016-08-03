from django.shortcuts import render

from django.http import Http404
from inventory.models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'inventory/index.html', {
        'items': items,
    })


def item_details(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item
    })


def full_image(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'inventory/full_image.html', {
        'item': item
    })
