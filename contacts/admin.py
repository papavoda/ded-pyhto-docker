from django.contrib import admin
from .models import About, ContactLink, Social


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['name', 'keywords', 'description', ]


@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'value',]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name',]