- # DAY08 

- 지난 이야기 

  - naver api 사용해보기 
    - 외부 사이트에 Request를 보낼 때, Post 방식으로 요청 하는 방법을 알았음 
    - Request Body 단순히 파라미터명과 파라미터 값으로 이루어진 싸이 아니라 json형식으로 파라미터를 보내는 방법
  - ORM 기초 
    - CREATE , READ를 DJANGO SHELL 에서 실행 시켜보기 
    - ORM(Object Relation Mapping)이 무엇인지 ? 왜 사용해 야 하는지 

- 오늘 이야기

  - 기본 게시판 만들기
    - URL 분리하기
    - URL.PY 에다가 우리가 접속할 모든 주소를 명시 했는데 CRUD 를 하다보면 만들어야 할 페이지가 점점 많아서구분하기가 어려워 직기 때문에 각 역활을 하는 APP마다 url.py파일을 생성할 예정 
    - 공용으로 사용할 수 있는 (공유할수 있는 )HTML 파일 만들기 
      - 반복되는 HTML 구조를 계속해서 새로 만들지 말고 , 공통되는 부분은 하나의 파일로 묶어서 반복해서 사용함 
        - CRUD 계속....해보고 익숙 해보자 !!!!!!!



- # ORM 기본 

- python manage.py makemigrations : DB 환경를만들수 있는 파일을 만든다 . 

- python manage.py migrate : 뼈대를 토대로 DB를 구축 한다. 

  

- URL을 분리 해서 관리해보자 

  ```python
  #지금 까지 배운 것은 URLS.PY에 모두 관리를 하고 이용 했다.
  #그러나 개발을 하면 할수록 URL이 많아지고 관리 하기 힘들어 진다. 
  #그래서 URL을 따로 관리 해보자 
  
  # 기존 urls.py 파일에서 
  from django.contrib import admin
  from django.urls import path,include #path와 include을 추가한다. 
  #include : 특정 url을 포함 하겠다.
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('boards/',include('borads.urls')) #main boards/만 입력 한다. 
  ]
  #새로 urls.py를 만들고 이 위치를 app안에 만들어준다.
  #내용은 다음과 같다. 
  from django.urls import path
  from .import views as boards_views #.import views .....을 찍어주자 
  urlpatterns = [
      #게시판의 메인페이지 , 전체 리스트 페이지 
      path('',boards_views.index),
      #게시판에 새 글을 작성 하는 페이지
      path('create',boards_views.create),
      path('new/',boards_views.new),
      #게시판 상세 페이지 
      path('<int:id>/',boards_views.show),
      #파라미터가 넘어올때 무조건 String로 넘어온다.그러나 우리가 쓰고 싶은건 intger를 써야 하므로 
      #형변환을 여기서 해주면 코드 작성시 형변환을 안해도 된다. 
      path('<int:id>/edit/',boards_views.edit),
      path('<int:id>/update/',boards_views.update),   
      path('<int:id>/delete/',boards_views.delete)    
  ]
  
  ```

  

  

- # python 에서 html 



```
기본 틀이 되는 html 파일을 base.html 만든다 . 
그리고 마지막 줄에 
{% block content %}
{% endblock %}
만든다. 
그리고 원하는 html 상에 기록 한다. 
{% extends 'base.html' %}
{% block content %}
<원하는 내용>
        {% endblock %} 
이렇게 만든다 
```



- Notion 한번 써보자 

- https://www.notion.so/product

  notion , 트렐로 , 

  https://www.atlassian.com/ko



- # Python CRUD

- C

  ```python
  def create(request):
      title =request.GET['title']
      contents=request.GET['contents']
      creator=request.GET['creator']
      #new_board = Board(title=title,contents=contents,creator=creator)
      #new_board.save()
      # 위 두줄을 하나로 만드는 또하나의 방법
      new_board = Board.objects.create(title=title,contents=contents,creator=creator)
      return redirect(f'/boards/{new_board.id}')
  	
  ```

  

  - NEW .HTML (HTML상에서 게시판 작성)

  ```python
  {% extends 'base.html' %}
  		{% block content %}
          <form action="/boards/create">
              <div class="form-group">
                  <label for="title">제목</label>
                  <input type="text" class="form-control" id="title" placeholder="제목을 입력하세요" 				name="title">
              </div>
  
              <div class="form-group">
                  <label for="contents">내용</label>
                  <textarea class="form-control" id="contents" rows="3" placeholder="내용" 						name="contents"></textarea>
              </div>
  
              <div class="form-group">
                      <label for="creator">작성자</label>
                      <input type="text" class="form-control" id="creator" name="creator">
                  </div>
              <div class="form-group text-center">
                  <input type="submit" value="작성하기" class="btn btn-primary">
              </div>
              </form>
              {% endblock %} 
  
  
  
  
  ```

  

SHOW(디테일 부분 )

```python
def show(request, id):
    board = Board.objects.get(id=id)
    context = {
        'board':board
    }
    return render(request,'show.html',context)
```

SHOW.HTML

```html
{% extends 'base.html'%}
{% block content %}
<h2>제목 :{{board.title}}</h2>

<h3>{{board.contents}}</h3>

<p>{{board.creator}}</p>
<div class="mt-3 text-center">
    <a href="/boards/{{board.id}}/edit" class="btn btn-danger">수정</a>
    <a href="/boards/{{board.id}}/delete" class="btn btn-warning text white">삭제</a>
</div>
{% endblock %} 
```

edit.python

```python

def edit(request,id):
    #원래 있던 내용이 들어 있는 form 
    board = Board.objects.get(id=id)
    context ={
        'board':board
    }
    return render(request,'edit.html',context)

```

edit.html(update)

```html
{% extends 'base.html' %}

{% block content %}
<form action="/boards/{{board.id}}/update">
    <div class="form-group">
        <label for="title">제목</label>
        <input type="text" class="form-control" id="title" placeholder="제목을 입력하세요" name="title" value="{{board.title}}">
    </div>

    <div class="form-group">
        <label for="contents">내용</label>
        <textarea class="form-control" id="contents" rows="3" placeholder="내용" name="contents">{{board.contents}}</textarea>
    </div>

    <div class="form-group">
            <label for="creator">작성자</label>
            <input type="text" class="form-control" id="creator" name="creator" value="{{board.creator}}" readonly>
        </div>
    <div class="form-group text-center">
        <input type="submit" value="작성하기" class="btn btn-primary">
    </div>
    </form>
{% endblock %}  
```

- update : 실제로 업데이트를 하는 파이썬 로직

  ```python
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
  ```

  

  - delete: 게시판을 삭제 

    ```python
    def delete(request,id):
        board = Board.objects.get(id=id)
        board.delete()
    
        return redirect('/boards')
    ```

    

  - index : 오늘 만든것에 메인 페이지이고 DB에 저장된 게시판을 모두 불러 온다. 

  ```python
  def index(request):
      #Boards 모델에 담긴 모든 글을 가져와서 보여줌 
      
      boards = Board.objects.all()
      context={
          'boards':boards
      }
      return render(request,'index.html',context)
  
  ```

  

- INDEX.HTML

  ```html
  {% extends 'base.html' %}
  
        {% block content %}
       
              <table class="table table-hover">
                      <thead>
                        <tr>
                          <th scope="col">#</th>
                          <th scope="col">제목</th>
                          <th scope="col">작성자</th>
                          <th scope="col">작성일자</th>
                        </tr>
                      </thead>
                      <tbody>
                        {% for board in boards%}
                        <tr onclick="location.href='/boards/{{board.id}}'">
                          <th scope="row">{{board.id}}</th>
                          <td>{{board.title}}</td>
                          <td>{{board.creator}}</td>
                          <td>2019-11-15</td>
                        </tr>
                        {% endfor%}
                      </tbody>
              </table>
                 <a href="/boards/new"> <button type="button" class="btn btn-primary">새글쓰기</button></a>
        
        {% endblock %} 
  ```

  

