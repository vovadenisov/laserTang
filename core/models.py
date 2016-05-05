# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(u'Название', max_length=255)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(u'Название', max_length=255)
    link = models.CharField(u'Ссылка', max_length=400)
    img = models.CharField(u'Ссылка на картинку', max_length=400)
    category = models.ForeignKey(
        Category, verbose_name=u"категория", blank=True, null=True, default=None, related_name="items"
    )

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'

    def __unicode__(self):
        return self.name