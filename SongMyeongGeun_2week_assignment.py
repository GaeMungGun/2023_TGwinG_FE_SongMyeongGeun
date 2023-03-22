# 1번
def sum(a, b):    
    return (a + b)

# 2번
def sub(a, b):
    return (a - b)

# 3번
def mul(a, b):
    return (a * b)

# 4번
def div(a, b):
    return (a / b)

# 5번
def distance(x1, y1, x2, y2):
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    return ((x + y) ** (1/2))

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    return (lylics[21:31])

# 7번
def reverseStr(string):
    return (string[::-1])

# 8번
def introduce():
    name = input("이름을 입력하세요 : ")
    hobby = input("취미를 입력하세요 : ")
    university = input("재학 중인 학교를 입력하세요 : ")
    birth_date = input("생일을 입력하세요 : ")
    introduce_myself = "제 이름은 {0}입니다. 취미는 {1}입니다. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다." .format(name, hobby, university,birth_date[3:4],birth_date[4:6])
    print(introduce_myself)

# 9번
def calc():
    a = int(input("첫 번째 수를 입력하세요 : "))
    b = int(input("두 번째 수를 입력하세요 : "))
    plus = "두 수의 합 : %d" % sum(a,b)
    print(plus)
    minus = "두 수의 차 : %d" % sub(a,b)
    print(minus)
    multiply = "두 수의 곱 : %d" % mul(a,b)
    print(multiply)
    share = "두 수의 몫 : %d" % (a % b)
    print(share)
