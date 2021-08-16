# from blog.blog.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=50)
    authorId = models.CharField(max_length=50,primary_key=True)
    likes = models.CharField(max_length=50)
    popularity = models.CharField(max_length=50)
    reads = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.author

