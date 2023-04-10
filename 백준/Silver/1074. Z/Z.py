N, r, c = map(int, input().split())

def z(N, r, c, q):
    if N == 0:
        return q
    half = 2 ** (N - 1)  # 절반의 길이
    if r < half:
        if c < half: # 1사분면
            quad = 1
        else: # 2사분면
            quad = 2
            c -= half # 다음 N-1에서의 위치를 위해 조정하자

    else:
        if c < half: # 3사분면
            quad = 3
            r -= half

        else: # 4사분면
            quad = 4
            r -= half
            c -= half
    # 현재 배열에서의 위치 앞에 있었던 사분면들의 숫자들을 더하자
    # ex) 4분면이면 3분면까지의 숫자들
    q += (quad - 1) * (half ** 2)

    # ex) 4분면이면 현재 4분면만의 배열로 다시 시작
    return (z(N - 1, r, c, q))

print(z(N, r, c, 0))
