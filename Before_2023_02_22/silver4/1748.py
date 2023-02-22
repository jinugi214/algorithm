import sys

input = sys.stdin.readline

N = int(input())

ans = 0

length = len(str(N)) # N의 길이

if length >= 2:
    for i in range(1, length):
        # N의 길이전의 값을 다 미리 더해준다.
        ans += 9 * 10**(-1+i) * i 
    
    # 마지막 N의 길이만 따로 구해서 더해준다.
    ans += (N - 10**(-1+length) + 1) * length
    
else:
    ans = N

print(ans)

'''
120 -> 252

1~9 -> 9 * 1
10~99 -> 90 * 2
100~120 -> 21 * 3

252 -> 648

1~9 -> 9 * 1
10 ~ 99 -> 90 * 2
100 ~ 252 -> 153 * 3

'''