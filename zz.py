import sys
input = sys.stdin.readline()

club = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT",
        "MOTION", "SPG", "COMON", "ALMIGHTY"]  # 동아리 리스트
max = []  # 선출된 후보들의 문제 개수 리스트

for _ in range(9):
    cap = list(int(input().split()))
    mNum = max(cap)
    max.append(mNum)
mIdx = max.index(mNum)
print(club[mIdx])
