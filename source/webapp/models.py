from django.db import models

STATUS_CHOICES = (
    ('active', 'активно'),
    ('blocked', 'заблокировано')
)


class Book(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(max_length=70, null=False, blank=False, verbose_name="email автора")
    text = models.TextField(max_length=1500, null=False, blank=False, verbose_name='Текст записи')
    CreatedDate = models.DateTimeField(auto_now=True)
    LastEditDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name="Статус",
                              default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)

    def __str__(self):
        return self.text