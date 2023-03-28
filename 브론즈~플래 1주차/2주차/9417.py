import sys
from itertools import combinations


def get_gcd(a, b):  # 최대 공약수
    while a % b != 0:
        a, b = b, a % b

    return b


for i in range(int(sys.stdin.readline())):
    max_n = -1
    arr = list(map(int, sys.stdin.readline().split()))
    combi = list(combinations(arr, 2))
    for com in combi:
        max_n = max(max_n, get_gcd(com[0], com[1]))
    print(max_n)
