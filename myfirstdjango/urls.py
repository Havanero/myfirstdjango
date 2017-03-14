from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from evil_dog_image import comments_view
from evil_dog_image import views
from myfirstdjango import settings

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^item/(?P<url_page>\w+)/(?P<item_id>\d+)/(?!.*api)(?!.*likes).*$',
                      views.item_details, name='item_detail'),
                  url(r'^list_paintings(?!.*api)(?!.*likes)', views.list_of_paintings, name='list_paintings'),
                  url(r'^list_charity(?!.*api)(?!.*likes)', views.list_of_charity_work, name='list_charity'),
                  url(r'^list_graphics(?!.*api)(?!.*likes)', views.list_of_graphics_work, name='list_graphics'),
                  url(r'api/likes',
                      comments_view.post_items_likes, name='post_items_likes'),
                  url(r'^(?P<url_page>\w+)/likes$', comments_view.get_all_page_likes, name='get_all_page_likes'),
                  url(r'^item/(?P<url_page>\w+)/(?P<item_id>\d+)/likes$', comments_view.get_items_likes, name='likes'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^static/(?P<path>.*)$', serve),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
