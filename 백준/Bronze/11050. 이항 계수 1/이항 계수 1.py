N, K = map(int, input().split())

# N! / K!(N-K)!

N_val = 1
for i in range(N, 0, -1):
    N_val *= i

K_val = 1
for i in range(K, 0, -1):
    K_val *= i

nk = N-K
NK_val = 1

for i in range(nk, 0, -1):
    NK_val *= i

print(N_val // (K_val * NK_val))