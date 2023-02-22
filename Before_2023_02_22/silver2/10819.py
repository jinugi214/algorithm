from itertools import permutations

num = input()
data = list(map(int, input().split()))

per = permutations(data)
max = 0

for i in per:
    s = 0
    for j in range(1, len(i)):
        s += abs(i[j-1] - i[j])
    if s > max:
        max = s

print(max)