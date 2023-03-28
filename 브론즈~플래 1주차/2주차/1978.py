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


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in arr:
    if is_prime(num):
        cnt += 1

print(cnt)
