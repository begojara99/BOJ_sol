for _ in range(int(input())):
    s = int(input())
    flag = 1
    for n in range(2, 1000001):
        if s % n == 0:
            flag = 0
            break
    # print(flag)
    print("YES" if flag else "NO")
