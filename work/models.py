from django.db import models
from django.urls import reverse


class article(models.Model):
    title=models.TextField(max_length=100,name="title",default="无标题")
    content=models.TextField(max_length=5000,name="content",default="...")
    date=models.DateTimeField(name="Date",auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('demo:page', kwargs={'pk': self.pk})
