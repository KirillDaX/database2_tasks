from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Author


def articles_list(request):
    template_name = 'articles/news.html'

    articles_selected = Article.objects.prefetch_related('author').defer('published_at')
    # прочтение документации и проведение тестовых игрищ
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.select_related


    context = {'object_list': articles_selected}

    return render(request, template_name, context)
