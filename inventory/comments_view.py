import json

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from inventory.comments import Likes
from inventory.models import Paintings, GraphicDesign, CharityDesign


def post_items_likes(request):
    if request.method == 'POST':
        print("original post url", request)
        incoming_data = json.loads(request.body.decode("utf-8"))
        item_id, page = extract_page_id(incoming_data.get('url'))
        charity_id, graphic_id, painting_id = return_page_id(item_id, page)
        like_page = Likes(facebook_user=incoming_data.get('user_name'),
                          likes_url=incoming_data.get('url'),
                          paintings=painting_id, graphics=graphic_id, charity=charity_id,
                          user_profile=incoming_data.get('picture_url'))
        like_page.save()
        print("done")
    return HttpResponse("OK")
    # return render(request, 'inventory/likes.html', {
    #     'likes': like_obj,
    # })


def get_items_likes(request, url_page, item_id):
    item = None
    target_page = None
    if 'charity_paint_details' == url_page:
        try:
            target_page = 'charity'
            item = Likes.objects.filter(charity_id=item_id)
            for it in item:
                print(it.facebook_user, '---', it.likes_url, '---', it.charity.image)
        except CharityDesign.DoesNotExist:
            raise Http404('This item does not exist')

    if 'paint_details' == url_page:
        try:
            target_page = 'paintings'
            item = Likes.objects.filter(paintings_id=item_id)
            # for it in item:
            #     print(it.facebook_user, '---', it.likes_url, '---', it.paintings.id)
        except Paintings.DoesNotExist:
            raise Http404('This item does not exist')

    if 'graphic_paint_details' == url_page:
        try:
            target_page = 'graphics'
            item = Likes.objects.filter(graphics_id=item_id)
            for it in item:
                print(it.facebook_user, '---', it.likes_url, '---', it.graphics.image)
        except GraphicDesign.DoesNotExist:
            raise Http404('This item does not exist')

    return render(request, 'inventory/single_likes.html', {
        'item': item, 'url_page': target_page,
    })


def get_all_page_likes(request, url_page):
    print("getting all Likes request for ", url_page)

    return HttpResponse("OK")


def extract_page_id(data):
    obj_str = json.dumps(data)
    print(obj_str)
    url = data.split("/")
    if url[len(url) - 1].isdigit():
        page_name = (url[len(url) - 1])
        item_id = (url[len(url) - 2])
    else:
        page_name = (url[len(url) - 2])
        item_id = (url[len(url) - 3])
    return page_name, item_id


def return_page_id(item_id, page):
    painting_id = None
    graphic_id = None
    charity_id = None
    if 'paint_details' == page:
        assert page == 'paint_details'
        painting_id = Paintings.objects.get(id=item_id)

    if 'graphic_paint_details' == page:
        assert page == 'graphic_paint_details'
        graphic_id = GraphicDesign.objects.get(id=item_id)

    if 'charity_paint_details' == page:
        assert page == 'charity_paint_details'
        charity_id = CharityDesign.objects.get(id=item_id)

    return charity_id, graphic_id, painting_id
