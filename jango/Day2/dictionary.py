
import random


a  = {
    "김민지":"070-6411-4545"
}
a["김민지"]

#print(a['김민지'])
#print(a.get("김민지"))

lunch_menu = {
    '20층 식당' : { 
        "A코스": "돈까스",
        "B코스": "순대국"
    },
    "양자강" : {
        '점심메뉴' : "양장피",
        '저녁특선' : "탕수육"
    },
    "대동집" : {
        "밥안주" : "비빔면",
        "술안주" : "오돌뼈"
    }
}

print(lunch_menu["20층 식당"]["B코스"])
print(lunch_menu.get("20층 식당").get("B코스"))

lunch_menu["경성불백"] = {
    "한식" : "석쇠불고기",
    "특식메뉴":"돈까스"
}


print(lunch_menu)
#lunch_menu["양자강"]= "자장면"
print(lunch_menu)

#모든 키 
print(lunch_menu.keys())
#value
print(lunch_menu.values())
#동시에
print(lunch_menu.items())

#b 안에서 순회 할때 마다 담는 곳은 a 
for key, value in lunch_menu.items():
    print(key)
    print(value)



print(random.choice(list(lunch_menu.keys())))
print(random.sample(list(lunch_menu.keys()), 2))


#if 조건1 :
  #  조건 1의 실행문
#elif 조건2:
    #조건 2의 실행문
#else:
    #나머지 실행문

    

















