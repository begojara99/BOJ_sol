res = 0
presum = 0
for i in range(10):
    n = int(input())
    res += n
    if res >= 100: 
        presum = res - n
        break  # 100이 넘는 순간 그 전과 후 값 비교하기 위해
if (res - 100) == (100 - presum): print(res)
else:
    print(res if (res-100) < (100-presum) else presum)