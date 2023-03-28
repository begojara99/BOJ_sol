def get_gcd(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


gcd, lcm = map(int, input().split())
temp = lcm // gcd
a, b = 1, temp
for i in range(1, temp//2 + 1):
    if temp % i == 0:
        c = i
        d = temp//i
        if get_gcd(c, d) != 1:
            continue
        if a+b > c+d:
            a = c
            b = d
print(a*gcd, b*gcd)
