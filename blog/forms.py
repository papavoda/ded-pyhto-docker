from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post
from ckeditor.fields import RichTextField


class PostCreateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'keywords',
                  'category', 'main_image', 'intro', 'text', 'status']
        # fields = '__all__'
        # exclude = ['pub_at', 'changed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок *', 'class': 'form-control bg-dark text-white'}),
            # 'description': forms.TextInput(attrs={'placeholder': 'Описание *', 'class': 'form-control'}),
            'keywords': forms.TextInput(
                attrs={'placeholder': 'Ключевые слова *', 'class': 'form-control bg-dark text-white'}),
            'intro': forms.Textarea(attrs={'placeholder': 'Интро *', 'class': 'form-control bg-dark text-white',
                                           'cols': '10',
                                           'rows': '5'}),

            'main_image': forms.ClearableFileInput(
                attrs={'class': 'form-control bg-dark text-white', 'multiple': False}),
        }

    images = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control bg-dark text-white', 'multiple': True})
                              )

    files = forms.FileField(required=False,
                            widget=forms.ClearableFileInput(
                                attrs={'class': 'form-control bg-dark text-white', 'multiple': True}))

    video_youtube = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                            'rows': 4, 'cols': 6, 'placeholder': 'Add <iframe></iframe> from Youtube'}))
