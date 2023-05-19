from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(Category)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "image", 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="80"')

    get_image.short_description = "Миниатюра"


class ImageInline(admin.StackedInline):
    model = Image
    max_num = 20
    extra = 0
    list_display = ("name", "image", 'get_image')
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="140" height="100"')


@admin.register(VideoYoutube)
class VideoYoutubeAdmin(admin.ModelAdmin):
    list_display = ("name", "video_frame")


class VideoYoutubeInline(admin.StackedInline):
    model = VideoYoutube
    max_num = 4
    extra = 0
    list_display = ("name", "video_frame",)


@admin.register(AudioInternal)
class AudioInternalAdmin(admin.ModelAdmin):
    list_display = ('name', 'track')


class AudioInternalInLine(admin.StackedInline):
    model = AudioInternal
    max_num = 20
    extra = 0
    list_display = ('name', 'track')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['created', 'title', 'slug', 'get_image', 'author', 'status']
    list_editable = ['status']
    readonly_fields = ("get_image",)
    inlines = [ImageInline, VideoYoutubeInline, AudioInternalInLine, ]
   # prepopulated_fields = {'slug': ('title',)}  # new

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.main_image.url} width="110" height="80"')
        except:
            return ''
