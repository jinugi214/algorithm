# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다
# 3중 for문을 이용
def lagrange(x):
    result = 4

    # 아래 모든 for문에서, 절반의 루트값 이하까지 보면 그 다음 for문에서 중복되므로,
    # root(해당 값) 부터 root(해당 값//2) 까지만 확인하면 된다.
    for i in range(int(n ** 0.5), int((n // 2) ** 0.5) - 1, -1):
        a = n - i * i
        if a == 0: return 1

        for j in range(int(a ** 0.5), int((a // 2) ** 0.5) - 1, -1):
            b = a - j * j
            if b == 0:
                result = min(result, 2)
                break

            for k in range(int(b ** 0.5), int((b // 2) ** 0.5) - 1, -1):
                c = b - k * k
                if c == 0:
                    result = min(result, 3)
                    break

    return result


n = int(input())
print(lagrange(n))