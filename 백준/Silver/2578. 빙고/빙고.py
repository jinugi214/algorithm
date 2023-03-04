def play(n):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                bingo[i][j] = 0


def check():
    cnt = 0
    # 가로
    for i in range(5):
        if bingo[i].count(0) == 5:
            cnt += 1
    # 세로
    for i in range(5):
        sero = 0
        for j in range(5):
            if bingo[j][i] == 0:
                sero += 1
            else:
                break
        else:
            if sero == 5:
                cnt += 1

    # 대각선
    tmp = 0
    for i in range(5):
        if bingo[i][i] == 0:
            tmp += 1
        else:
            break
    else:
        if tmp == 5:
            cnt += 1

    tmp = 0
    # 0,4 -> 1,3, 2,2 3,1 4,0
    for i in range(5):
        if bingo[i][4 - i] == 0:
            tmp += 1
        else:
            break
    else:
        if tmp == 5:
            cnt += 1
        
    if cnt >= 3:
        return True


bingo = [list(map(int, input().split())) for _ in range(5)]

nums = [list(map(int, input().split())) for _ in range(5)]

ans = 0
brk = False
for i in range(5):
    for j in range(5):
        play(nums[i][j])
        ans += 1
        if i >= 2 and check():
            print(ans)
            brk = True
            break
    if brk:
        break
