import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Article name', max_length=250)  # VARCHAR
    author_name = models.CharField('Article author', max_length=100, default='Elena Sivuda')
    article_text = models.TextField('Main text')  # LongCHAR
    pub_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.article_title

    def was_public_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Связь с статьей, при удалении все снести
    author_name = models.CharField('Commentator name', max_length=100)
    comment_text = models.CharField('Comment text', max_length=300)

    def __str__(self):
        return self.author_name


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'