a,b,n,w = map(int,input().split())
li = []
for i in range(1,n):
    if(a*i + b*(n-i)==w):
        li.append([i,n-i])
if len(li) != 1: print(-1)
else: print(f"{li[0][0]} {li[0][1]}")