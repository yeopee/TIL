from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Article ,Comment, AticlesImages, Board
import json
# Create your views here.


def js_test(request):
    return render(request, 'js_test.html')



def jq_test(request):
    boards = Board.objects.all().order_by("created_at").reverse()
    context = {
        'boards':boards
    }
    return render(request,'jq_test.html',context)


def submit_boards(request):
    if request.method == "POST":
        contents = request.POST["board"]
        boards = Board.objects.create(contents=contents)
        context = {
            'boards':boards
        }
        return render(request, 'empty.html',context)

def delete_boards(request):
    if request.method =='POST':
        id = request.POST["board_id"]
        board = Board.objects.get(id=id)
        board.delete()
        context = {
            'board_id' : id
        }
        
        return HttpResponse(json.dumps(context),content_type="application/json") 

def edit_boards(request):
    if request.method =='POST':
        id = request.POST["board_id"]
        contents = request.POST["contents"]
        board = Board.objects.get(id=id)
        board.contents = contents
        board.save()

        return HttpResponse('',status=204)
        

def index(request):
    if request.method=="POST":
        article = Article()
        article.contents = request.POST["contents"]
        #원본이미지를 받을떄
        #article.image = request.FILES["image"]
        #원본 이미지를 프로세싱 한 이미지를 저장 
        #article.image_resized = request.FILES["image"]
        article.save()
        for image in request.FILES.getlist("image"):
            AticlesImages.objects.create(article_id=article.id, image=image)
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

        if request.POST["form_Method"]=="create":
            comment = Comment()
        elif request.POST["form_Method"]=="edit":
            comment_id = request.POST["comment_id"]
            comment = Comment.objects.get(id=comment_id)
        comment.contents=contents
        comment.article_id = article_id
        comment.save()
        context={
            'Method': request.POST["form_Method"],
            'comment': comment.contents,
            'comment_id':comment.id,
            'article_id': comment.article_id,
        }
    return render(request,'comment.html',context)



def delete_comment(request):
    if request.method == 'POST':
        id = request.POST["comment_id"]
        comment = Comment.objects.get(id=id)
        comment.delete()
        context = {
            'comment_id' : id
        }
        return HttpResponse(json.dumps(context),content_type="application/json")

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