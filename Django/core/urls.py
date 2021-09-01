from django.urls import path
from django.views.generic import TemplateView

from .views import main



urlpatterns = [
    path('', main),
    #path('', TemplateView.as_view(template_name='/example/index.html')),
]
