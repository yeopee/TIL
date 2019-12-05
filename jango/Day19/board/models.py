from django.db import models
from faker import Faker
from django.conf import settings
# Create your models here.
f = Faker()
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=50)
    email= models.CharField(max_length=200)
    content = models.TextField()
    date= models.DateField(blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles') #article_set


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(
                title=f.text(20),
                content=f.text(),
                keyword=f.company(),
                email=f.email(),
            )

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)