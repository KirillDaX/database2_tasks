from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleToTag


class ArticleToTagInline(admin.TabularInline):
    model = ArticleToTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleToTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ArticleToTagInline]


class ArticleToTagInlineFormSet(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # Везде фолс, если одна уже была, то не дожно срабатывать
            if form.cleaned_data['main_tag']:
                test = form.errors
                # your custom formset validation
                # пока не понимаю как организовать этот механизм в админке без форм.
                # по дукоментации так, по примеру не так
                # мало конкретики, clean_data в формах выгядит явно иначе,
                # только на создание или только на апдейт?
                raise ValidationError(_('Тут всегда ошибка'), code='ищем второй главный раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода





