from itertools import permutations
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = list(permutations(arr, 3))
for _ in range(int(input())):
    guess, st, ba = map(int, input().split())
    guess = list(str(guess))
    rem_cnt = 0
    for i in range(len(num)):
        print("Z")
