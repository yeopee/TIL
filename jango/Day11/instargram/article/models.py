from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill,Thumbnail
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.  

class Article(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="article_likes")

    #원본 이미지 저장
    #image = models.ImageField(blank=True)
   
    #수정된 이미지도 할수 있다.
    # image_resized = ProcessedImageField(
    #   #  source = 'image',
    #     upload_to = 'articles/images',
    #     processors = [ResizeToFill(200,300)],
    #     format='JPEG',
    #     options={'quality':90}
    # )


    #이미지에 썸내일을 생성해줌
    #media/CACHE 원본 이미지의 썸네일을 자동생성
    # image_thumbnail = ImageSpecField(
    #     source='image',
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality':90}
    # )
    def comments(self):
        return Comment.objects.filter(article_id=self.id)
    def article_images(self):
        return AticlesImages.objects.filter(article_id=self.id)
    def check_permitted(self, target_id):
        return self.user_id == target_id


class HashTag(models.Model):
    tag = models.CharField(max_length=16, unique=True)
    article = models.ManyToManyField(Article,related_name="tags")





class AticlesImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    image_thumbnail= ImageSpecField(
        source='image',
        processors=[Thumbnail(300,300)],
        format='JPEG',
        options={'quality':90}
    )



class Comment(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    

class Board(models.Model):
    contents = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
