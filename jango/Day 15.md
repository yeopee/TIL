- # Day 15 

  - JS ,JQUERY 

    - 요소를 찾아서 
    - ㅇ요소에 이벤트가 발생하는 것을 포착해서 (EVENT LISTENER)
    - 이벤트가 발생 했을때 어떤 로직을 실행 할지 결정 (Event handler)

  - Ajax

    - 비동기 js & xml

    - Callback 을 받아서 실행 한다 .

    - ```html
      <script>
          $(function(){
              $.ajax({
                  url: '어느 주소로 요청 하는지 ',
                  method:'어떤 request method로 보낼지',
                  data:{
                      key:'어떤 형태로 보낼지',
                  },
                  success:function(data){
                      '요청이 성공적으로 완료 됬을떄'
                  },
                  error:function(data){
                      '요청이 정상적으로 완료 되지 않을떄 '
                  }
              })
          })
          
      </script>   
      ```

      - 댓글 수정 

        - 수정 버튼을 누른다 .
        - 원래의 댓글 내용이 입력창에 들어간다 . 
        - 확인 버튼을 누르면 수정한 내용이 반영된다. 

        ```
        방법 1-확인 버튼에 속성을 추가해서 제출 할 떄 해당 속성에 유무를 파악해 서로 다른 로직을 탈수 있도록 한다
        방법 2-수정할 떄 ajax 제출하는 url 부분을 변수 (html 속성)로 만들어서 처리한다. 
        
        이미 submit 댓글 등록 한다 . 
        어디로 보낼지 등록한 것을 변수로 만든다 .	
        
        ```

        

      이벤트 발생 

      - js로 html 요소를 추가한 다음 ajax로 서버에 요청을 통해 실제 db 에 반영
      - ajax로 서버에 요청을 보내 실제 db에 반영되고 나면 js로 html 요소 추가 

  - Auth (User)