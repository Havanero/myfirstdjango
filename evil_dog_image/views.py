from django.http import Http404
from django.shortcuts import render

from evil_dog_image.models import Paintings, CharityDesign, GraphicDesign


def index(request):
    items = Paintings.objects.all()
    return render(request, 'evil_dog_image/index.html', {
        'items': items,
    })


def list_of_paintings(request):
    items = Paintings.objects.all()
    return render(request, 'evil_dog_image/list_paintings.html', {
        'items': items,
    })


def item_details(request, item_id, url_page):
    item = None
    previous_url = None
    if 'charity_paint_details' == url_page:
        try:
            previous_url = 'list_charity'
            item = CharityDesign.objects.get(id=item_id)
        except CharityDesign.DoesNotExist:
            raise Http404('This item does not exist')

    if 'paint_details' == url_page:
        try:
            previous_url = 'list_paintings'
            item = Paintings.objects.get(id=item_id)
        except Paintings.DoesNotExist:
            raise Http404('This item does not exist')

    if 'graphic_paint_details' == url_page:
        try:
            previous_url = 'list_graphics'
            item = GraphicDesign.objects.get(id=item_id)
        except GraphicDesign.DoesNotExist:
            raise Http404('This item does not exist')

    return render(request, 'evil_dog_image/item_detail.html', {
        'item': item, 'previous_url': previous_url,
    })


def full_image(request, item_id):
    try:
        item = Paintings.objects.get(id=item_id)
    except Paintings.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'evil_dog_image/full_image.html', {
        'item': item
    })


def list_of_charity_work(request):
    items = CharityDesign.objects.all()
    return render(request, 'evil_dog_image/list_charity.html', {
        'items': items,
    })


def list_of_graphics_work(request):
    items = GraphicDesign.objects.all()
    return render(request, 'evil_dog_image/list_graphics.html', {
        'items': items,
    })
