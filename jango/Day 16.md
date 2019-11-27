#   Day16



create comment

form으로 부터 내용을 받아서 코멘트를 작성한다 

article 별로 있는 form 으로 부터 

submit 이라는 이벤트에 

해당 form 에 있느 input중에서 텍스트를 입력한 

내용을 받아서 create comment 역할을 하는 url 

```html
$('.commentForm').on.('sumbit',function(){
e.preventDefault();
var contents=$(this).find('input.commentInput').val()
//어떤 article에 대한 댓글인지 알아야함
var id = $(this).find('input.articleId').val()
$.ajax({
url:'{% url "comment" %}',
method:'POST',
data:{
contenrs: contents,
csrfmiddlewaretoken:'{{csrf_token}}'
article_id: id 
},
success: function(data){
console.log("성공");
console.log(data);
var comment =`
<li class="list-group-item" id="comment-{{comment.id}}"><i class="fas fa-comment"></i> ${data.comment}<span class="float-right"><a href="" class="btn btn-warning"><i class="fas fa-edit"></i></a>
<button class="btn btn-danger commentDelete" data-id=><i class="fas fa-trash-alt"></i></button>
 </span> 
 </li>
`
$('.lsit-group').apprnd(comment);
},
error: function(data){
console.log("실패");
}
})

})
```

```
view.py
context ={
'comment':comment.contents
'comment_id':comment.id
}
return HttpResponse(json.dumps(context),content_type="application/json")


```





# Auth

```
/accounts/login
/accounts/logout
/accounts/signup
```

Http req/res  무상태성 : 너에게 요청 한후 그 뒤는 남남이다. 

cookie :  내 브라우저  브라우저가 종료되면 .......날라간다고 ..한다 .보안에 취약하다. 

차이 :정보저장의 주체 

session: 서버 컴퓨터 -> 메모리등 ,db등 

내컴 :정보의 위치만 가지고 있음 

서버컴 : 응답을 보내준다 . 정보를 저장 





















