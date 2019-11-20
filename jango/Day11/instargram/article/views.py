from django.shortcuts import render,redirect
from .models import Article ,Comment

# Create your views here.
def index(request):
    if request.method=="POST":
        article = Article()
        article.contents = request.POST["contents"]
        article.save()
        return redirect('articles')
    else:
        articles = Article.objects.all().order_by("created_at").reverse()
        context={
            'articles':articles
        }
        return render(request,'index.html',context)


def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method=='POST':
        article.contents =request.POST["contents"]
        article.save()
        return redirect('articles')
    else:
        context={
        'article':article
        }
        return render(request,'article/edit.html',context)

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles')



def comments(request):
    if request.method =='POST':
        contents = request.POST["contents"]
        article_id = request.POST["article_id"]
        comment = Comment()
        comment.contents=contents
        comment.article_id = article_id
        comment.save()
        return redirect('articles')


def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles')

def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method =='POST':
        comment.contents = request.POST["contents"]
        comment.save()
        return redirect('articles')
    else:
        context = {
            'comment':comment
        }
        return render(request, 'comment/edit.html',context)