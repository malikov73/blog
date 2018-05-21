from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article, Category
from django.shortcuts import render_to_response


class home(generic.ListView):
    context_object_name = 'article_list'
    model = Article
    template_name = 'blog/home.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()[:3]
        context['category2'] = Category.objects.all()[3:]
        return context


class PostDetail(generic.DetailView):
    model = Article
    template_name = 'blog/post_detail.html'


class CategoryPostFilter(generic.ListView):
    template_name = 'blog/home.html'

    def get_queryset(self):
        self.slug = get_object_or_404(Category, name=self.kwargs['slug'])
        return Article.objects.filter(category=self.slug)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f"context {context}, object_list {object_list}, kwargs {args} ")
        return context


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

        return render_to_response('home/index.html', context)
        
class home(generic.View):
    context_object_name = 'Article'
    def get(self, request):
        context = {}
        all_articles = Article.objects.order_by('-created')
        current_page = Paginator(all_articles, 2)
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
        return render_to_response('blog/home.html', context)        
        """
