from django.shortcuts import render,redirect
from .models import Board
# Create your views here.
# 게시글 제목 ,내용 , 작성자  

def index(request):
    #Boards 모델에 담긴 모든 글을 가져와서 보여줌 
    
    boards = Board.objects.all()
    context={
        'boards':boards
    }
    return render(request,'index.html',context)

def new(request):

    return render(request,'new.html')


def create(request):
    title =request.GET['title']
    contents=request.GET['contents']
    creator=request.GET['creator']
    #new_board = Board(title=title,contents=contents,creator=creator)
    #new_board.save()
    # 위 두줄을 하나로 만드는 또하나의 방법
    new_board = Board.objects.create(title=title,contents=contents,creator=creator)
    return redirect(f'/boards/{new_board.id}')

    
def show(request, id):
    board = Board.objects.get(id=id)
    context = {
        'board':board
    }
    return render(request,'show.html',context)

def edit(request,id):
    #원래 있던 내용이 들어 있는 form 
    board = Board.objects.get(id=id)
    context ={
        'board':board
    }
    return render(request,'edit.html',context)

def update(request,id):
    #실제로 update가 일어나는곳
    board = Board.objects.get(id=id)#id가 id인 녀석을 불러라 
    title =request.GET['title']
    contents=request.GET['contents']
    board.title=title
    board.contents = contents
    board.save() 
    
    return redirect(f'/boards/{board.id}')
    #다른 페이지로 옮겨라 

def delete(request,id):
    board = Board.objects.get(id=id)
    board.delete()

    return redirect('/boards')