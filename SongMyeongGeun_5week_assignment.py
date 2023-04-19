# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분
import math

def calcCircleArea(r):
    result = round(pow(r, 2) * math.pi, 2)
    return result

def calcLog(a, b):
    result = round(math.log(b,a), 2)
    return result

def calcSin(x):
    result = round(math.sin(x), 2)
    return result

def calcFactorial(x):
    result = math.factorial(x)
    return result

def calcCombination(n, r):
    result = math.comb(n, r)
    return result

def calculator(order):
    answer = 0

    if (order[0:4] == "원넓이:"):
        answer = calcCircleArea(float(order[5:]))

    elif (order[0:3] == "로그:"):
        if (order[4] == "e"):
            answer = calcLog(math.e, float(order[6:]))

        else:
            for i in range(4,len(order)):
                if (order[i] == " "):
                    count = i
                    break
                else:
                    continue

            answer = calcLog(float(order[4:count]), float(order[count+1:]))

    elif (order[0:3] == "사인:"):
        answer = calcSin(float(order[4:]))

    elif (order[0:5] == "팩토리얼:"):
        answer = calcFactorial(int(order[6:]))

    elif (order[0:3] == "조합:"):
        for i in range(4,len(order)):
                if (order[i] == " "):
                    count = i
                    break
                else:
                    continue

        answer = calcCombination(int(order[4:count]), int(order[count+1:]))

    else:
        answer = "정확한 양식으로 입력해주십시오"

    return answer
