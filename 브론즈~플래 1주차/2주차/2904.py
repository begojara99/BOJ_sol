# 소인수 분해 후 그것들의 배수를 구한다
# 각 소수의 승수를 N으로 나눠준다

import math


def divi(n):  # 소인수분해
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            print(i)
            n //= i

    if n != 1:
        print(n)
