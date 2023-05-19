from ckeditor.fields import RichTextField
from django.db import models


class Social(models.Model):
    """класс модели соц сетей сраницы о нас"""
    icon = models.ImageField(upload_to="icons/social/", default='', blank=True, null=True)
    icon_dark = models.ImageField(upload_to="icons/social/", default='', blank=True, null=True)
    font_awesome_code = models.CharField(max_length=12, default='', blank=True, null=True)
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.FileField(upload_to="icons/contacts/", null=True, blank=True)
    name = models.CharField(max_length=100)  # address, phone, email
    value = models.CharField(max_length=100, default='')  # Street, 903-1234567,
    font_awesome_icon = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('pk', )

    def __str__(self):
        return self.name


class About(models.Model):
    """Класс модели страницы о нас"""
    keywords = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=300, default='')
    name = models.CharField(max_length=25)
    main_image = models.ImageField(upload_to="about/", default='',
                                   help_text="add main about img 1280x853")
    text = RichTextField(max_length=6000)

    def __str__(self):
        return f'{str(self.id)} - {self.name}'
