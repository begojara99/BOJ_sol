# 소인수 분해를 구하는데 2까지만 구해서 cnt 구해서 2^cnt 하면 될듯

import sys


def two_prime(n):  # 소인수 분해를 하는척 2로만 분해해서 2^cnt 반환
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return 2 ** cnt


a, b = map(int, sys.stdin.readline().split())
res = 0
for i in range(a, b+1):
    res += two_prime(i)
print(res)
