r = int(input())
data = list(map(int, input().split()))

def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    per = []
        
    def generate(chosen, used):
        if len(chosen) == r:
            per.append(list(chosen))
            return
    
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return per
    
per = permutation(data, r)
max = 0

for i in per:
    s = 0
    for j in range(1, len(i)):
        s += abs(i[j-1] - i[j])
    if s > max:
        max = s

print(max)