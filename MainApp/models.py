from django.db import models
from django.contrib.auth.models import User


LANG_CHOICES = (
    ('python', 'python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
)


class Snippet(models.Model):
    class Meta:
        ordering = ["name", "lang"]
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)


class Comment(models.Model):
   text =models.TextField(max_length=1000)
   creation_date = models.DateTimeField(auto_now=True)
   author = models.ForeignKey(to=User, on_delete=models.CASCADE)
   snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name="comments")