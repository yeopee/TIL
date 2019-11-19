from django.db import models

# Create your models here.

class Board(models.Model):
    title=models.CharField(max_length=16)
    contents=models.TextField()
    creator=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):

        return f'[{self.title}]-created by {self.creator}'

    

    def datetime_to_string(self):
        return self.created_at.strftime("%Y-%m-%d")

    def created_by(self):
        return f'이 글은 {self.creator}님이 작성했습니다.'