from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView


from .models import Post, Category, Image, AudioInternal
from contacts.models import About
from .forms import PostCreateForm



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.select_related('category').filter(status='published',
                                                                                 category__name='Новости').order_by(
            '-created')[:5]
        # context['categories'] = Category.objects.
        context['about_home'] = About.objects.first()
        # context['contact_us_form'] = ContactUsForm
        context['title'] = 'Сайт московской рок-группы Дед ПыхтО'
        context['nbar'] = 'home'
        return context


#  !!!! ListView  !!!!
class NewsListView(ListView):
    template_name = 'blog/post_list.html'
    # context_object_name = 'post_list'
    paginate_by = 9
    queryset = Post.objects.select_related('category', 'author').filter(category__name='Новости',
                                                                        status='published').order_by(
        '-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'news_list'
        return context


class MusicListView(NewsListView):
    queryset = Post.objects.select_related('category', 'author').filter(category__name='Музыка',
                                                                        status='published').order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'music_list'
        return context


class PhotoListView(NewsListView):
    queryset = Post.objects.select_related('category', 'author').filter(category__name='Фото',
                                                                        status='published').order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'photo_list'
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    # slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = CommentForm
        self.object.views += 1
        self.object.save()
        context['images'] = self.object.get_images
        context['youtube'] = self.object.get_youtube
        context['audio_internal'] = self.object.get_audio_internal
        context['uploaded_files'] = self.object.get_uploaded_files
        # context['comments'] = self.object.get_comments
        return context


class DraftsListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Post.objects.select_related('category', 'author').filter(author=self.request.user,
                                                                        status='draft').order_by('-created')


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()

        images = self.request.FILES.getlist('images')
        for image in images:
            Image.objects.create(post=post, image=image)

        files = self.request.FILES.getlist('files')
        for file in files:
            AudioInternal.objects.create(post=post, track=file)

        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCreateForm
        context['main_title'] = 'Добавление статьи'
        context['nabr'] = 'new-post'
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    # form_class = PostCreateForm
    template_name = 'blog/post_update.html'

    fields = ['title', 'keywords',
              'category', 'main_image', 'intro', 'text', 'status', ]

    #### TODO Add possible change files, image etc
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.get_images
        context['youtube'] = self.object.get_youtube
        context['audio_internal'] = self.object.get_audio_internal
        return context
    # def get_object(self, queryset=None):
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #     return get_object_or_404(queryset, audio_internal=self.kwargs['pk'])


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')


# class MusicListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.select_related('category', 'author').filter(category__name='Музыка',
#                                                                         status='published').order_by('-created')
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.select_related('category', 'author').filter(category__name='Музыка',
#                                                                         status='published').order_by('-created')
#     serializer_class = PostSerializer


