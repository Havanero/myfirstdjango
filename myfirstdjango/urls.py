from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<item_id>\d+)/', views.item_details, name='item_detail'),
    url(r'^admin/', admin.site.urls),
]
