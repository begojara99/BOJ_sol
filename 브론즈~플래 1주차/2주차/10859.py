# 소수판별
import math
import sys
n = int(sys.stdin.readline())


def is_prime(num):
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            cnt += 1

    if num == 1 or cnt != 0:
        return 0
    return 1


if n == 2 or n == 5:
    print("yes")
else:
    str_n = str(n)
    if '3' in str_n or '4' in str_n or '7' in str_n or str_n[0] == '5' or str_n[0] == '9' or str_n[0] == '8':
        print("no")
    elif is_prime(n):  # 입력받은 수 소수(1단계 통과) -> 180도 뒤집은 수 검사
        arr = list(map(str, str_n))
        arr.reverse()
        for i in range(len(arr)):
            if arr[i] == '6':
                arr[i] = '9'
            elif arr[i] == '9':
                arr[i] = '6'
        arr = int(''.join(arr))
        if is_prime(arr):
            print("yes")
        else:
            print("no")
    else:
        print("no")
