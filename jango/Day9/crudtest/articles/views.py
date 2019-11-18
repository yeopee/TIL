from django.shortcuts import render, redirect

from .models import Article
# Create your views here.

def index(request):
    # Article Model 에 있는 모든 Article을 불러옴
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def show(request, id):
    # Article Model 에서 특정 id를 가진 하나의 Article을 불러옴
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'show.html', context)

def new(request):
    # 불러올 Article 없음
    return render(request, 'new.html')

def create(request):
    # Article을 새로 생성
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']
    # 방법1
    # article = Article.objects.create(title=title, contents=contents, creator=creator)
    # 방법2
    article = Article()
    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()

    return redirect('show', article.id)

def edit(request, id):
    # Article Model 에 있는 특정 Article을 가져와야 함
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'edit.html', context)

def update(request, id):
    # Article Model 에 있는 특정 Article을 가져와야 함
    article = Article.objects.get(id=id)
    # 기존 article 정보를 바꿔서 저장하는 부분
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']

    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()

    return redirect('show',article.id)

def delete(request, id):
    # Article Model 에 있는 특정 Article을 가져와야 함
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('index')