import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))
cnt = 0
for j in range(1, n+1):
    for i in range(1, j+1):
        if((sum(arr[0:j+1]) - sum(arr[0:i])) == k):
            cnt += 1
print(cnt)
