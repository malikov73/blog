from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone

from .models import Article


class home(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'Article'

    def get_queryset(self):
        """Return the last five pubished questions."""
        return Article.objects.order_by('-created')
