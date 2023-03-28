# 실질적 약수
import math
import sys
n = int(sys.stdin.readline())


def is_prime(num):  # 소수
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            cnt += 1

    if num == 1 or cnt != 0:
        return 0
    return 1


def sod(n):  # 실질적 약수 합
    if n == 1 or is_prime(n):  # 1이거나 소수이면 실질적 약수의 합이 0이다
        return 0

    arr = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n // i:
                arr.append(n // i)
    return (sum(arr)-1-n)


def csod(n):  # sod의 합
    res = 0
    for i in range(1, n+1):
        res += sod(i)
    return res


print(csod(n) % 1000000)
