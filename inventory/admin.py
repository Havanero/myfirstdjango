from django.contrib import admin

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
