from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from inventory import views
from myfirstdjango import settings

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^item/(?P<item_id>\d+)/', views.item_details, name='item_detail'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^static/(?P<path>.*)$',
                      'django.views.static.serve')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
