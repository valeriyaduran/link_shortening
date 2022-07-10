from django.contrib import admin

from links.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin_link', 'shortened_link')
    list_display_links = ('id', 'origin_link', 'shortened_link')
    search_fields = ('id', 'origin_link', 'shortened_link')
    ordering = ['id']


admin.site.register(Link)
