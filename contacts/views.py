from django.views.generic import TemplateView, DetailView
from .models import About, ContactLink


class AboutView(TemplateView):
    template_name = 'contacts/about.html'

    # context_object_name = 'about'
    # queryset = About.objects.all()[1:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.order_by('id')[1:]
        # context['categories'] = Category.objects.all()
        # context['hero_one'] = HomeHeroSlogans.objects.all()
        # context['contact_us_form'] = ContactUsForm
        # context['title'] = 'Правильный ремонт квартир'
        context['nbar'] = 'about'
        return context


class ContactLinkView(TemplateView):
    template_name = 'contacts/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactLink.objects.all()
        # context['categories'] = Category.objects.all()
        # context['hero_one'] = HomeHeroSlogans.objects.all()
        # context['contact_us_form'] = ContactUsForm
        # context['title'] = 'Правильный ремонт квартир'
        context['nbar'] = 'contact'
        return context
