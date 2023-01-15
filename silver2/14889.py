from sys import stdin


def cal_diff(team_list: list) -> None:
    another_team_list = list(set(range(N)) - set(team_list))
    team_sum = 0
    for i, v in enumerate(team_list[:-1]): # for문을 이용해 사전순으로 능력치를 더해준다.
        for v2 in team_list[i + 1:]:
            team_sum += stats[v][v2] + stats[v2][v]

    another_team_sum = 0
    for i, v in enumerate(another_team_list[:-1]):
        for v2 in another_team_list[i + 1:]:
            another_team_sum += stats[v][v2] + stats[v2][v]

    ans.append(abs(team_sum - another_team_sum))

    return None


def dfs(team_list: list) -> None:
    if len(team_list) == N / 2: # 팀을 절반으로 나눈 수라면
        cal_diff(team_list)
        return None

    for i in range(team_list[-1] + 1 if team_list else 0, N): # 순서가 상관없기 때문에 사전순으로 팀을 구성
        if team_list and team_list[0] != 0: # 0번째 사람을 포함하여 팀을 구성하는 수만 구한다면 모든 경우를 구한 것이기 때문
            return None
        team_list.append(i)
        dfs(team_list)
        team_list.pop()


N = int(stdin.readline())
stats = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = []
dfs([])
print(min(ans))