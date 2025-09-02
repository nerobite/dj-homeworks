from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    #tags = models.ManyToManyField('Tag', through='Scope', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    def __str__(self):
        return self.name

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='РАЗДЕЛ')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='ОСНОВНОЙ')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'ТЕМАТИКИ СТАТЕЙ'
    def __str__(self):
        return self.tag.name