import sys
input = sys.stdin.readline

m = 0
m_idx = 0
arr = [0 for _ in range(1001)]  # 기둥
for _ in range(int(input())):
    l, h = map(int, input().split())
    arr[l] = h
    if m < h:  # 가장 높은 기둥
        m_idx = l
        m = h
cur = 0
ans = 0
for i in range(m_idx+1):  # 왼쪽 그룹
    cur = max(cur, arr[i])
    ans += cur
cur = 0
for i in range(1000, m_idx, -1):  # 오른쪽 그룹
    cur = max(cur, arr[i])
    ans += cur
print(ans)
