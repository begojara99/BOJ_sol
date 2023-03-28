import math
import sys


def is_prime(num):  # 소수
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            cnt += 1

    if num == 1 or cnt != 0:
        return 0
    return 1


a, b, d = map(int, sys.stdin.readline().split())
cnt = 0
for n in range(a, b+1):
    if is_prime(n):
        if str(d) in str(n):
            cnt += 1
print(cnt)
