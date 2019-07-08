## Spring 설정하기

1. 다이다믹 웹 프로젝트를 생성 
2. 스프링 네이쳐를 눌러 스프링을 사용 할수있게 한다. 
3.maven (add spring lib)를 구축한다. 
3-1 pom.xml(list up Lib)을 수정한다. 
3-2 라이브러리는 다운받는다 . MAVEN 에서 스프링 업데이트를 한다. 

### Spring ioc (제어의 역행)

//not ioc 스파게티 코드 





1.XML 
Java 코드를 수정하지 않고 XML 파일의 설정만 변경하면 됨 ∴ 유지보수가 편리
하지만 Java 코드에 의존관계와 관련된 어떤 메타 데이터도 없으므로 XML 설정을 해석해야만 무슨 객체가 의존성 주입이 되었는지 확인할 수 있음

2.Annotation
XML 설정에 대한 부담도 없고, 의존관계에 대한 정보가 코드 내에 들어있기 때문에 사용하기 편함
하지만 의존성 주입할 객체의 이름이 코드에 명시되어야 하므로 반드시 수정이 필요함







### Spring Aop (관계지향 프로그래밍)





공통로직을 분리 함으로써응집도가 높게 개발할 수 있도록 지원한다. 

유지 보수를 혁신적으로 향상시킬 수 있다 .

책 그림 2-6 참고 

2-6: 보안 코드를넣어야 한다면각자3개에 넣고 각자 코드를 수정해야 한다. 그러나 aop를 사용 하면 각각의 클라스에 코딩을 안해도 된다.

 

-spring의 구조는 6조 구조 이미지 참고 



<bean>
2-1. <bean> 의 class, id 속성
둘은 이미 써봤다. id는 사용자가 객체를 불러내기 위한 고유의 이름이어야 한다는 점을 제외하면 가볍게 넘어갈 수 있을 것 같다.

<bean> 의 init-method, destroy-method 속성
init-method는 특별히 초기화할 함수를 정의했을 때 컨테이너에게 해당 Class의 초기화 작업을 지시할 수 있다. 반대로 destroy-method는 컨테이너가 객체를 삭제하기 직전에 호출될 임의의 메소드를 지정할 수 있다.


2-3. <bean>의 lazy-init 속성
<bean>은 기본적으로 pre-loading 속성을 지니고 있다고 한다. 그 말뜻은 사용자가 사용하기 이전에 이미 객체화하여 미리 준비한다는 뜻이다. 그래서 시스템에 무리가 된다고 판단이 되는 경우에는 lazy-init 속성을 true로 설정하여 사용자가 사용하려고 객체를 불러낼 경우에 생성하게 할 수 있다. 메모리 관리에 구조적으로 접근할 수 있다는 뜻이다.



의존성 주입 :Stv,Ltv 그리고 스피커 예시 활용 



### AOP (Aspect Oriented Programming)



AOP를 이해하는 데 가장 중요한 핵심 개념이 바로 관심 분리(Separation of Concerns)
횡단 관심(Crosscutting Concerns) : 메소드마다 공통으로 등장하는 로깅이나 예외, 트랜젝션 처리 같은 코드
핵심 관심(Core Concerns) : 사용자의 요청에 따라 실제로 수행되는 핵심 비즈니스 로직
따라서 AOP는 기능을 구분한 후, 핵심 관심에 영향을 미치지 않고 횡단 관심을 잘 끼워넣도록 하는 개발 방법 → 공통 모듈인 횡단 관심을 코드 밖에 설정한 후 끼워넣음
		


 @Autowired, @Qualifier


 Speaker 인터페이스를 사용한 클래스 AppleSpeaker와 SonySpeaker 클래스가 있었다. 이 경우에 @Autowired를 하게 되면 콤포넌트 id로 apple, sony로 등록한 두개의 클래스중에 어떤 인스턴스를 선택해서 
적용해야할지 모르기 때문에 에러가 발생하게 된다. 이런경우에는 @Qualifier로 해결한다.


모호한 객체의 주입을 피하는 것이다. 이렇게 하면 원하는 객체를 주입할 수 있어서 좋지만,
 2줄로 항상 관리해야한다는 불편함이 따른다. 그래서 @Resource를 사용하기도 한다.

 @Resource 어노테이션은 속성값으로 @Component의 id값을 입력해주어야 한다. 



#### 참고 할것 




Mapper: mybatis에 들어갈 통로 역활



user xml 


dao-mapper -xml


viewResolver = view 폴더에.jsp에 만 붙혀주면 알아서찾겠다 .

ModelAndView: data 와 화면

viewResolver: 이름만 넣으면 찾아준다. mvc:interceptors 사용자가 접속 했을때 main 랭귀지를  해준다 .	

messageSource: 다국어 처리 

Trandactional = db 에 오류가 생기면 그전 상황으로 돌아간다. 