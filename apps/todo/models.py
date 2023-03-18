# Django
from django.db import models

# Third-Party
from auths.models import Client


class Tasks(models.Model):
    """Tasks model."""
    TO_DO: int = 0
    DONE: int = 1
    PROGRESS_CHOICES: tuple = (
        (TO_DO, 'To do'),
        (DONE, 'Done'),
    )
    progress: int = models.SmallIntegerField(
        verbose_name='progress',
        choices=PROGRESS_CHOICES,
        default=TO_DO
    )
    publisher: Client = models.ForeignKey(
        verbose_name='publisher',
        to=Client,
        on_delete=models.RESTRICT,
        null=True,
    )
    title: str = models.CharField(
        verbose_name='title',
        max_length=30,
        null=True
    )
    description: str = models.TextField(
        verbose_name='description',
        null=True
    )

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = (
            'progress',
        )
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
