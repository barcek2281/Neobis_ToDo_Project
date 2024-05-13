from django.db import models


class ToDo(models.Model):
    title = models.CharField('Названия задания', max_length=500, blank=False)
    is_complite = models.BooleanField('Завершенно', default=False)

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задание'

    def __str__(self):
        return self.title
