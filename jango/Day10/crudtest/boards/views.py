from django.shortcuts import render,redirect
from .models import Board

# Create your views here.

def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }

    return render(request,'index.html',context)

def show(request,id):
    boards = Board.objects.get(id=id)
    context = {
        'board': boards
    }
    return render(request, 'show.html', context)
def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']
        board =Board.objects.create(title=title,contents=contents,creator=creator)
        return redirect('boards:show', board.id)

    else:    
        return render(request, 'new.html')

        

# def create(request):
#     title = request.GET['title']
#     contents = request.GET['contents']
#     creator = request.GET['creator']
#     # 방법1
#     # article = Article.objects.create(title=title, contents=contents, creator=creator)
#     # 방법2
#     board = Board()
#     board.title = title
#     board.contents = contents
#     board.creator = creator
#     board.save()
#     return redirect('boards:show', board.id)

def edit(request,id):
    board = Board.objects.get(id=id)
    if  request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']

        board.title = title
        board.contents = contents
        board.creator = creator
        board.save()
        return redirect('boards:show',board.id)
    else:
        context = {
            'board': board
        }
        return render(request, 'edit.html', context)

# def update(request, id):
#     # Article Model 에 있는 특정 Article을 가져와야 함
#     board = Board.objects.get(id=id)
#     # 기존 article 정보를 바꿔서 저장하는 부분
#     title = request.GET['title']
#     contents = request.GET['contents']
#     creator = request.GET['creator']

#     board.title = title
#     board.contents = contents
#     board.creator = creator
#     board.save()

#     return redirect('boards:show',board.id)

def delete(request, id):
    # Article Model 에 있는 특정 Article을 가져와야 함
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('boards:index')