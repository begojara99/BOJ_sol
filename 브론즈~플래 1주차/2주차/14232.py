# 소인수분해
import math
n = int(input())

arr = []

for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        arr.append(i)
        n //= i

if n != 1:
    arr.append(n)

arr.sort()
print(len(arr))
print(*arr)
