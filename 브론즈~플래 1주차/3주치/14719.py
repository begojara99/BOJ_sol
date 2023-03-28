import sys
input = sys.stdin.readline

m = 0
m_idx = 0
h, w = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 기둥
for i in range(1, w+1):
    if m < arr[i]:  # 가장 높은 기둥
        m_idx = i
        m = arr[i]
cur = 0
ans = 0
for i in range(m_idx+1):  # 왼쪽 그룹
    cur = max(cur, arr[i])
    ans += cur
cur = 0
for i in range(w, m_idx, -1):  # 오른쪽 그룹
    cur = max(cur, arr[i])
    ans += cur
print(ans - sum(arr))
