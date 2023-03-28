import sys
input = sys.stdin.readline
n, h = map(int, input().split())

bot = [0] * (h + 1)  # 석순
top = [0] * (h + 1)  # 종유석
min_cnt = n  # 파괴해야 하는 장애물의 최소값
range_cnt = 0  # 최소값이 나타나는 구간의 수

for i in range(n):
    if i % 2 == 0:
        bot[int(input())] += 1
    else:
        top[int(input())] += 1

for i in range(h - 1, 0, -1):
    bot[i] += bot[i + 1]
    top[i] += top[i + 1]

for i in range(1, h + 1):

    if min_cnt > (bot[i] + top[h - i + 1]):
        min_cnt = (bot[i] + top[h - i + 1])
        range_cnt = 1
    elif min_cnt == (bot[i] + top[h - i + 1]):
        range_cnt += 1

print(min_cnt, range_cnt)
