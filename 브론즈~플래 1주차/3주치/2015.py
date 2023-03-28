import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

prefix = [0]  # 누적합 저장할 리스트

for i in range(1, n + 1):
    prefix.append(prefix[i - 1] + arr[i])
cnt = {}
ans = 0
for i in range(n + 1):
    ans += cnt.get(prefix[i] - k, 0)

    cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1

print(ans)
