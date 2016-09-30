from django.contrib import admin

from inventory.comments import Likes
from .models import Paintings, GraphicDesign, CharityDesign


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'image', 'datetime']


admin.site.register(Paintings, ItemAdmin)


class GraphicItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'image', 'datetime']


admin.site.register(GraphicDesign, GraphicItemAdmin)


class CharityItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'image', 'datetime']


admin.site.register(CharityDesign, CharityItemAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['facebook_user', 'likes_url', 'user_profile', 'paintings', 'graphics', 'charity', 'datetime']


admin.site.register(Likes, LikeAdmin)
