from django.urls import path

from . import views
from .views import AboutView

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactLinkView.as_view(), name='contact'),
    ]
