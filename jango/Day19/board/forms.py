from django import forms

from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, strip=True)
    email = forms.EmailField()
    keyword = forms.CharField(min_length=1, max_length=10)
    class Meta:
        model = Article
        #fields ='__all__'   
        #exclue는 이걸 빼고 내보내겠습니다. 
        exclude = ['date','author','like_users']
   
class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=1,max_length=200)
    class Meta:
        model = Comment
        fields = ['content',]