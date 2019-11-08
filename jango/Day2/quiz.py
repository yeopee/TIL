
score= {
    "수학":90,
    "국어" : 87,
    "한국지리": 92
}

print(round(sum(score.values()) / len(score)),2)

scores = {
    "a학생" : {
        "수학": 80,
        "영어": 72,
        "한국지리":42
    },
    "b학생" : {
        "수학" : 22,
        "영어" : 32,
        "한국지리" : 53

    }

}




for key,value in scores.items():
    print(key)
    print(value)
