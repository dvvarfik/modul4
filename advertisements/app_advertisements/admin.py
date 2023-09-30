from django.contrib import admin
from .models import Advertisements
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "created_date", "updated_date", "image"]
    list_filter = ["auction", "created_at", "updated_at"]
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.display(description='Thumbnail')
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" width="50" />', obj.image.url)
        return format_html('<img src="{}" height="50" width="50" />', '/static/img/adv.png')

    list_display = ['title', 'price', 'thumbnail']

    @admin.action(description = "Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisements, AdvertisementAdmin)