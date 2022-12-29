from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from django.db import models
from django.urls import reverse_lazy


class MenuItem(MPTTModel):
    """модель элемента меню"""

    title = models.CharField("Заголовок", max_length=64)
    parent = TreeForeignKey("self", on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')

    def get_absolute_url(self):
        return reverse_lazy('menu-retrieve', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'
