li = list(map(int, input().split()))
n = min(li)  # 초기값
while True:
    cnt = 0
    for i in range(5):
        if n % li[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1
