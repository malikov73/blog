from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article
from django.shortcuts import render_to_response


class home(generic.View):
    context_object_name = 'Article'
    def get(self, request):
        context = {}
        """Return the last five pubished questions."""
        all_articles = Article.objects.order_by('-created')
        current_page = Paginator(all_articles, 1)
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['article_lists'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['article_lists'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['article_lists'] = current_page.page(current_page.num_pages)
        # be careful here is the shit code
        if context['article_lists'].has_next():
            context['never'] = context['article_lists'].next_page_number()
        else:
            context['never_disabled'] = 'disabled'
        if context['article_lists'].has_previous():
            context['older'] = context['article_lists'].previous_page_number()
        else:
            context['older_disabled'] = 'disabled'
        print(context['article_lists'].has_next())
        return render_to_response(''
                                  'blog/home.html', context)

class PostDetail(generic.DetailView):
    model = Article
    template_name = 'blog/post_detail.html'
"""
class EIndexView(View):

    def get(self, request):
        context = {}
        # Забираем все опубликованные статье отсортировав их по дате публикации
        all_articles = Article.objects.filter(article_status=True).order_by('-article_date')
        # Создаём Paginator, в который передаём статьи и указываем, 
        # что их будет 10 штук на одну страницу
        current_page = Paginator(all_articles, 10)

        # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
        # "GET /?page=2 HTTP/1.0" 200,
        # Поэтому нужно забрать page и попытаться передать его в Paginator, 
        # для нахождения страницы
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['article_lists'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['article_lists'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['article_lists'] = current_page.page(current_page.num_pages)

        return render_to_response('home/index.html', context)"""