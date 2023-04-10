# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    lst_len = len(lst)
    count = 0

    for i in range(lst_len):
        for j in range(lst_len):
            if (lst[i] * 2 == lst[j]):
                count += 1
    
    return count

# 2번
def pascal(n):
    psc_arr = [[1 for j in range(i+1)] for i in range(n)]

    if (n > 2):
        for i in range(2, n):
            for j in range(1, i):
                psc_arr[i][j] = psc_arr[i-1][j-1] + psc_arr[i-1][j]

    return psc_arr[n-1]

# 3번
def beerRefrigerator(n):
    count = 0

    surface_area = []
    surface_area_str = []
    divisor_list = [i for i in range(1, n+1) if n % i == 0]

    for i in range(len(divisor_list)):
        for j in range(len(divisor_list)):
            for k in range(len(divisor_list)):
                if (divisor_list[i] * divisor_list[j] * divisor_list[k] == n):
                    x = divisor_list[i]
                    y = divisor_list[j]
                    z = divisor_list[k]
                    surface_area.append(x * y * 2 + y * z * 2 + z * x * 2)
                    a = str(x)
                    b = str(y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                    c = str(z)
                    surface_area_str.append(c + ' X ' + b + ' X ' + a)

    while True:
        if (min(surface_area) == surface_area[count]):
            break
        else:
            count += 1

    return surface_area_str[count]

# 4번
def matrixMul(mat1, mat2):
    a = len(mat1)
    b1 = len(mat1[0])
    b2 = len(mat2)
    c = len(mat2[0])

    for i in range(a):
        if (b1 != len(mat1[i])):
            return '행렬의 곱셈을 진행 할 수 없습니다'
        
    for i in range(b2):
        if (c != len(mat2[i])):
            return '행렬의 곱셈을 진행 할 수 없습니다'

    if (b1 != b2):
        return '행렬의 곱셈을 진행 할 수 없습니다'

    result_matrix = [[0 for j in range(c)] for i in range(a)]

    for i in range(a):
        for j in range(c):
            for k in range(b1):
                result_matrix[i][j] += mat1[i][k] * mat2[k][j]

    return result_matrix