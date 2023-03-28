# (0,0)에서 보이지 않으려면 직선의 기울기가 달라야 한다.
# 4/2나 6/3은 약분하면 둘 다 기울기가 2로 똑같다.
# #따라서 분자와 분모의 최대공약수가 1인 값들을 찾아내면 된다.

def get_gcd(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


arr = [0 for _ in range(1001)]
arr[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j:
            continue

        if get_gcd(i, j) == 1:
            cnt += 2
    arr[i] = arr[i-1] + cnt

for _ in range(int(input())):
    n = int(input())

    print(arr[n])
