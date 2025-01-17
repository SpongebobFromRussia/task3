from django.db import models

# Create your models here.

class ToDo(models.Model):
    tittle = models.CharField('Название задания', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)
    user = models.CharField('name', max_length=50)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.tittle    