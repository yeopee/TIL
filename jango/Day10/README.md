# 

- # DAY 10 



#  RestFUL api 

| 역활   | Request-method                                               | end-point             | views(function) | 기존역활    |
| ------ | ------------------------------------------------------------ | --------------------- | --------------- | ----------- |
| new    | GET                                                          | /articles/new/        | new             | 새글 form   |
| create | POST                                                         | /articles/            | new             | 새글작성    |
| show   | GET                                                          | /articles/<id>        | show            | 한개 글보기 |
| read   | GET                                                          | /articles             | index           | 전체리스트  |
| update | GET                                                          | /articles/<id>/edit   | edit            | 수정 form   |
| update | POST                                                         | /articles/<id>edit    | edit            | 수정 반영   |
| delete | POST(DELETE)->GET 방식 사용함 (왜냐하면 A태그는 GET 방식 요청만 가능 ) | /articles/<id>/delete | delete          | 삭제        |



crsf token