import sys

input = sys.stdin.readline

N = int(input())

data = [list(map(int, input().rstrip())) for _ in range(N)]

# 우선 4분면으로 나누자
# 1~4분면을 확인
# 0또는 1로 같은 숫자로 되어있을 경우
# 0 또는 1 출력
# 같은 숫자로 안되어 있을 경우
# ()를 만들고 재귀를 통해서 해당 사분면을 다시 4분면으로 나누고 탐색
# 더이상 탐색을 안해도 되거나 한개만 남았을 경우 return


rlt = []


def dfs(x, y, z):
    val = data[x][y]

    flag = 0
    for i in range(x, x + z):
        if flag:
            break
        for j in range(y, y + z):
            if data[i][j] != val:
                flag = 1
                break

    if flag:
        rlt.append('(')
        # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
        dfs(x, y, z // 2)
        dfs(x, y + z // 2, z // 2)
        dfs(x + z // 2, y, z // 2)
        dfs(x + z // 2, y + z // 2, z // 2)
        rlt.append(')')
    else:
        rlt.append(val)


dfs(0, 0, N)

print(''.join(map(str, rlt)))
