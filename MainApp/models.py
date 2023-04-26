from django.db import models


LANG_CHOICES = (
    ('python', 'python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
)


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
