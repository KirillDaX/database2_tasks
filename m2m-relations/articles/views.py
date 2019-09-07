from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Tag, ArticleToTag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    test = Tag.objects.filter(articletotag__main_tag=True).order_by('-articles__published_at')
    all_tags = Tag.objects.all().values
    arts_with_main = ArticleToTag.objects.filter(main_tag=True).values

    context = {'object_list': object_list,
               'test': test,
               'arts_with_main': arts_with_main,
               'all_tags': all_tags}

    return render(request, template, context)

