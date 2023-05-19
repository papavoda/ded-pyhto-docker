from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify  # ne
from django.urls import reverse
from mutagen.easyid3 import EasyID3
from .validators import validate_file_extension


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        # '<slug:slug>/<slug:post_slug>'
        return reverse("category_detail", kwargs={'pk': self.pk})


def upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'articles/{instance.author}/{instance.slug}/{filename}'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    description = models.CharField(max_length=500, default='', blank=True, verbose_name='Краткое описание')
    keywords = models.CharField(max_length=100, default='', blank=True, verbose_name='Ключевые слова')
    # slug = models.SlugField(max_length=64, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='Автор')
    category = models.ForeignKey(Category, related_name="post", verbose_name='Категория',
                                 help_text='Выберите категорию',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 )
    main_image = models.ImageField(upload_to=upload_directory_path, verbose_name='Главное изображение', null=True,
                                   blank=True)
    # image = models.ImageField(upload_to='articles/%Y/%m/%d/%pk', null=True, blank=True)

    intro = models.TextField(max_length=500, default='', verbose_name='Вступительный текст',
                             null=True, blank=True)
    # RichTextField -> for ckeditor
    text = RichTextField(max_length=8000, null=True, blank=True, verbose_name='Основной текст', )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Обновлено', )
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',
                              verbose_name='Статус публикации')
    views = models.BigIntegerField(default=0, null=True, blank=True, verbose_name='Количество просмотров', )

    class Meta:
        ordering = ('-created',)

    app_name = __package__

    def get_absolute_url(self):
        return reverse("post_detail",
                       kwargs={'app_name': self.app_name, 'cat_slug': self.category.slug, 'slug': self.slug})

    # def get_comments(self):
    #     return self.comment.all().filter(active=True)

    def get_images(self):
        return self.images.all()

    def get_youtube(self):
        return self.youtube.all()

    def get_audio_internal(self):
        return self.audio_internal.order_by('tracknumber')

    def get_uploaded_files(self):
        return self.uploaded_files.all()

    def save(self, *args, **kwargs):  # new
        self.description = self.title
        # if not self.slug:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category} - {self.title}'


# for Image upload
def upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/instance.post.author/instance.post.slug/<filename>
    return f'articles/{instance.post.author}/{instance.post.slug}/{filename}'


class Image(models.Model):
    name = models.CharField(max_length=250, default='', null=True, blank=True)  # alt
    post = models.ForeignKey(Post, related_name='images', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=upload_directory, validators=[validate_file_extension])

    def __str__(self):
        return f'{self.name} - {self.image}'


class VideoYoutube(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название видео', default='Видео', blank=True, null=True)
    post = models.ForeignKey(Post, related_name='youtube', on_delete=models.SET_NULL, null=True)
    video_frame = models.TextField(max_length=900)

    def __str__(self):
        if self.name:
            return self.name


class AudioInternal(models.Model):
    name = models.CharField(max_length=250, default='Unknown', verbose_name='Название песни')
    post = models.ForeignKey(Post, related_name='audio_internal', on_delete=models.SET_NULL, null=True)
    tracknumber = models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер')
    track = models.FileField(upload_to=upload_directory, verbose_name='Аудио файл',
                             validators=[validate_file_extension])
    site_play = models.BooleanField(default=False, verbose_name='Встроенный проигрыватель', )

    def save(self, *args, **kwargs):
        # if not self.tracknumber:
        # Extract track number from MP3 file
        try:
            # Load the file and get its tags
            mp3 = EasyID3(self.track)
            self.tracknumber = int(mp3.get("tracknumber", [""])[0].split('/')[0])
            self.name = mp3.get("title", [""])[0]

        except Exception as e:
            print('Error extracting track number:', e)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.tracknumber} - {self.name} ({self.track})'


class UploadFile(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя файла')
    post = models.ForeignKey(Post, related_name='uploaded_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_directory, verbose_name='Альбом целиком',
                            validators=[validate_file_extension], blank=True, null=True)
    link = models.CharField(max_length=500, verbose_name='Ссылка на скачивание', blank=True, null=True)
    annotations = models.CharField(max_length=255, default='Скачать весь альбом', verbose_name='Скачать целиком итп')

    def __str__(self):
        # f = self.file.split('/')[-1]
        return f'{self.file}'
# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)
#     # website = models.URLField(max_length=200, null=True, blank=True)
#     message = models.TextField(max_length=500)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)
#     # default_avatar = models.ImageField(default='')
#
#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.name, self.post)
