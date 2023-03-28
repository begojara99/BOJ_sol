n, m = map(int, input().split())


def count_number(n, k):  # 팩토리얼에서 원하는 수 승수 구하기
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt


five_count = count_number(n, 5) - count_number(m, 5) - count_number(n - m, 5)
two_count = count_number(n, 2) - count_number(m, 2) - count_number(n - m, 2)

answer = min(five_count, two_count)
print(answer)
