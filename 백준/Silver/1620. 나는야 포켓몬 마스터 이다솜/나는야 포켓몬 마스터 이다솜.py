import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을
# 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력

dogam1 = {}
dogam2 = {}

for i in range(1, N+1):
    name = input().rstrip()
    dogam1[i] = name
    dogam2[name] = i
for i in range(M):
    val = input().rstrip()
    if val.isdigit():
        idx = int(val)
        print(dogam1[idx])
    else:
        print(dogam2[val])