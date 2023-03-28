import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
presum = [0]
temp = 0
for i in arr:
    temp += i
    presum.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(presum[j]-presum[i-1])
