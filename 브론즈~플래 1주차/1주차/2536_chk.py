arr = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1
res = 0
for row in arr:
    res += row.count(1)
print(res)

# 2차 배열 한번에 카운팅 못해서 한줄씩 카운팅해야함
