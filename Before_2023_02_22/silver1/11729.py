# 이동 횟수의 경우 
# n개의 원판을 이동시킬 때 n - 1 원판을 이동시킨 후 
# 제일 밑에 있는 원판을 이동시킨다.
# 그리고 다시 n - 1 원판을 이동시킨다.

def cnt(n):
    if n == 1:
        return 1
    else:
        return cnt(n-1)*2 + 1

# 맨 밑에 있는 원반을 제외하고 모두 보조기둥으로 옮겨야 한다
# 이후 맨 밑에 있는 원반을 목표기둥으로 옮긴 후에는 n-1로 진행해도 된다.
# 그리고 원래 시작기둥이였던 기둥에는 아무것도 없기 때문에 보조기둥으로
# 원래 보조기둥이였던 기둥에 나머지 원반들이 있기 때문에 시작기둥이 된다.
def hanoi(n, start, end, backup):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, backup, end)
    print(start, end)
    hanoi(n - 1, backup, end, start)

n = int(input())
print(cnt(n))
hanoi(n, 1, 3, 2)
