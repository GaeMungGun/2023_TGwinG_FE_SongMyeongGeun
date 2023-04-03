# 1번
def grade(score):
    if (score > 100):
        return 'Put the number between 0~100'
    elif (score >= 90):
        return 'A'
    elif (score >= 80):
        return 'B'
    elif (score >= 70):
        return 'C'
    elif (score >= 60):
        return 'D'
    else:
        return 'F'
    
# 2번
def quadrant(x, y):
    if (x > 0 and y > 0):
        return '제 1사분면'
    elif (x < 0 and y > 0):
        return '제 2사분면'
    elif (x < 0 and y < 0):
        return '제 3사분면'
    elif (x > 0 and y < 0):
        return '제 4사분면'

# 3번
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0):
        return '윤년입니다.'
    elif (year % 100 == 0 and year % 400 != 0):
        return '윤년이 아닙니다.'
    elif (year % 400 == 0):
        return '윤년입니다.'
    else:
        return '윤년이 아닙니다.'

# 4번
def dice(a, b, c):
    if (a == b == c):
        return (10000 + a * 1000)
    elif (a == b or a == c):
        return (1000 + a * 100)
    elif (b == c):
        return (1000 + b * 100)
    else:
        return (max(a,b,c) * 100)

# 5번
def alarm(time):
    if (time < 100):
        time += 2400
    elif (time > 2400):
        return '값을 올바르게 적어주세요'

    minute = time % 100

    if (minute < 45):
        earlytime = time - 85
    else:
        earlytime = time - 45

    jungwootime = str(earlytime)
    
    if (len(jungwootime) == 3):
        if (jungwootime[1] == '0' and jungwootime[2] == '0'):
            return jungwootime[0] + '시 '
        elif (jungwootime[1] == '0'):
            return jungwootime[0] + '시 ' + jungwootime[2] + '분'
        else:
            return jungwootime[0] + '시 ' + jungwootime[1:3] + '분'
    
    elif (len(jungwootime) == 4):
        if (jungwootime[2] == '0' and jungwootime[3] == '0'):
            return jungwootime[0:2] + '시 '
        elif (jungwootime[2] == '0'):
            return jungwootime[0:2] + '시 ' + jungwootime[3] + '분'
        else:
            return jungwootime[0:2] + '시 ' + jungwootime[2:4] + '분'
