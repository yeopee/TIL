# DAY 19 

 



- 어딘가 올린다 . 
- full?
- 용량은 돈이다... 
- 프로젝트 환경관리가 잘 안된다. 
- 독립환겨을 구성 해야 한다 . 
- virtual 환경 (독립 환경)

이걸 왜하냐? 

다른 컴퓨터에서 프로그램을 돌리라면은 우리가 pip install 한거를 다 깔아야 돌릴수 있다. 

그래서 독립적인 환경을 구성해야 한다.

 

```
python -m venv venv
source venv/Scripts/acrivate
f1 = > Select Interpreter
touch .gitignore # (venv/ +)
pip install django
pip freeze > requirement.txt

mac os 에서 가상 환경 활성화 

source venv/bin.activate
```

pip freeze : 버젼을 얼린다 . 

!+tab : html:5을 자동 완성 한다. 

block +tab +esc 는 block을 자동 생성 한다 .

DIRS : 이친구를 먼저 base.html 찾는다 # default installed app 안에  temlpeates 을 찾는 다 

$ python manage.py shell_plus --print-sql : power shell 로 orm 이 어떻게 구동 되는지 볼수 있다 .

