from itertools import combinations
li = []
for _ in range(9):
   li.append(int(input())) 
combi = list(combinations(li, 7))
for com in combi:
    if sum(com)==100:
        a=sorted(list(com))
        for n in a:
            print(n)
        break