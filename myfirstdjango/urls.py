from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from inventory import views
from myfirstdjango import settings

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^list_paintings', views.list_of_paintings, name='list_paintings'),
                  url(r'^item/(?P<url_page>\w+)/(?P<item_id>\d+)/', views.item_details, name='item_detail'),
                  url(r'^list_charity', views.list_of_charity_work, name='list_charity'),
                  url(r'^list_graphics', views.list_of_graphics_work, name='list_graphics'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^static/(?P<path>.*)$', serve)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
