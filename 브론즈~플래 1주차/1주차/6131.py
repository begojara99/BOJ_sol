n = int(input())
li=[]
for a in range(1,501):
    for b in range(1,a+1):
        if (a-b)*(a+b) == n:
            li.append(a)
print(len(li))
        