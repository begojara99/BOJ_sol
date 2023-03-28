n = int(input())
cnt = 0
for i in range(101):#택희
    for j in range(101):#영훈
        for k in range(101):#남규
            if i+j+k != n: continue
            if not k >= j + 2: continue    
            if i == 0 or j == 0 or k == 0: continue   
            if i % 2 == 1: continue 
            cnt+=1
print(cnt)