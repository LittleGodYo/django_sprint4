from django.db import models


class PublishedModel(models.Model):
    """
    Абстрактная модель `PublishedModel`
    добавляет функциональность публикации объектов.
    """

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True


class CreatedModel(models.Model):
    """
    Абстрактная модель `CreatedModel`
    добавляет информацию о времени создания объекта.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True
