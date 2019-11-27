



- # Day11 

- # 오늘 이야기 

- 오늘 ~금까지 1개의 프로젝트로 수업 진행 

- instagram!

- 댓글 (comment):model,url,

  - database relation(1:N)

- 이미지 업로드 (내일)

  - 좋아요,해시 태그 database relation(M:N)

유저 한명이 여러개의 게시글을 만든다 .(1:N)

게시글은 1에 대한 정보를 가지고 있다. ID (FK)(USER_ID)



render :  첫번쨰 인자 request  동일한 수준에 template 폴더 안에서 html 을 찾는다 .

이안에 파이썬 문법이 있는것 부터 찾는다. 

{% %} 파이썬 로직 

{{}} 실제 출력 (내용,태그)

- 게시판 댓글 구현 





- 오늘 배운건 확실히 이해하고 git 업데이트 하기

  

  - # 이어서

  - #  Day12

  - static file 정적인 파일 이미 준비된 이미지 

    - 개발 환경 vs 배포 환경
      - 실제 위치랑 보여지는 위치는 다르다 

  - 이미지 업로드 

    - 모델 하나에 직접입력 
    - 이미지 리사이징
    - 이미지 썸네일

  -  multiple 이미지 업로드 

    - 하나의 article에 여러 이미지 업로드 하기 

  - js 기본 

    - 하나의 페이지를 동적으로 만든다 .
    - JQuery - > JS 프레임워크(X) JS 라이브러리 (O)



# DAY13

오늘 이야기 

-  기본 JS + JQuery
-  css selector (.className. #D)
-  EVENT
-  DOM
-  사용이유 
  -  페이지를 다이나믹하게 만들기 위해서 사용 
  -  클라이언트 단에서 데이터를 관리 
  -  요소 찾기 - 해당요소에 이벤트를 먹이기 
  -  이벤트 발생 - 어떠한 변화가 생김 (색상이 바뀐다거나 생거나 사라지단거나 여러가지 변화 )
  -  일부 부분에서 발생한 변화를 서버에 저장, 수정 ,삭제 (ajax)
  -  월요일에는 JS + AUTH (로그인) 할 예정 
-  AUTH(login)
  -  

​	



4가지 이벤트 확인 

```html
console.log("hello world");
VM198:1 hello world
undefined
alert("굿모닝");
undefined
confirm("굿모닝이니 ???");
true
confirm("굿모닝이니 ???");
true
confirm("굿모닝이니 ???");
false
prompt
ƒ prompt() { [native code] }
prompt("당신의 이름은 무엇입니까");

```



document: 우리에게 날라온 html 

window : document 에 상위 버전 

location.href 

document.getElement



요소 찾기 

```
document.getElementById('joke');
<h2 id=​"joke">​GOOD MORNING​</h2>​
document
#document
document.getElementsByClassName('element');
HTMLCollection(5) [p.element, p.element, p.element, p.element, p.element]0: p.element1: p.element2: p.element3: p.element4: p.elementlength: 5__proto__: HTMLCollection
리턴 타입 배열이다 	
document.querySelector('.element') 하나를 꺼낸다 class_name
<p class=​"element">​요소1​</p>​
document.querySelectorAll('.element') 모두 꺼낸다.


document.querySelectorAll('.p-list > .element')
document.querySelectorAll('.p-list > span')
document.querySelectorAll('.p-list, span')

```



요소 이벤트 리스너 달기 ('이벤트명',function(나는 핸들러입니다.){

})

- 이벤트 발생 

```
element.classList.toggle('bg-red');
누르면 상황이 바뀜 
var pList = document.getElementsByTagName('p');
        console.log(pList);
        var pList2 = document.querySelectorAll('p');
        console.log(pList2);
        pList2.forEach(function(element){
            element.addEventListener('click',function(){
                if(confirm("이태그를 삭제하겠습니까?")){
                  //  element.setAttribute('class','bg-red')
                    
                  element.classList.toggle('bg-red');
                    
                }
               // element.setAttribute('class', 'p-tag');
            })
        })


console.dir : 그안에 속성도 다 찍어준다 /

appendChild : 맨 마지막 에 생긴다 . 

prepend: 맨 처음에 생긴다 . 


```



