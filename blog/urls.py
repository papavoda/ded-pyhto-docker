from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import *
from blog.sitemap import PostSitemap, StaticSitemap

sitemaps = {
    'posts': PostSitemap,
    'static': StaticSitemap,
}


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/news/', NewsListView.as_view(), name='news_list'),
    path('blog/music/', MusicListView.as_view(), name='music_list'),
    path('blog/photo/', PhotoListView.as_view(), name='photo_list'),
    path('blog/drafts/', DraftsListView.as_view(), name='drafts'),
    path('<str:app_name>/<slug:cat_slug>/<slug:slug>', PostDetailView.as_view(), name="post_detail"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('blog/post-create/', PostCreateView.as_view(), name='post_create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    # path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    # path("", MusicListAPIView.as_view(), name="post_list"),
    # path("<int:pk>/", PostDetail.as_view(), name="post_detail"),

]

