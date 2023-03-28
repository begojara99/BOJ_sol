n, a = map(int, input().split())
cnt = 0
x = a
while x <= n:
    cnt += n // x
    x *= a
print(cnt)
