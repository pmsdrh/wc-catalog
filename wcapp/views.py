from django.views.generic.base import TemplateView
from wcapi.api import products

# Create your views here.
class ProductsView(TemplateView):
    template_name = "wcapp/maintable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = products().show_all()


        return context
