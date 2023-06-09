from django.db import models


class Comment(models.Model):
    text = models.TextField(blank=False) #нельзя отправлять пустой комментарий
    date_of_create = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=32)
    published = models.BooleanField(default=False) #премодерация

    def __str__(self):
        return self.text [ :32] + '...'
    
    class Meta:
        ordering = ('-date_of_create', )
