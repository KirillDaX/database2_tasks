from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField('Tag', blank=True, related_name='articles', through='ArticleToTag',
                                 verbose_name='Название раздела')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return f'{self.title}'


class ArticleToTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Выбор разделов')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='выбрать раздел')
    main_tag = models.BooleanField(verbose_name='Основной')
