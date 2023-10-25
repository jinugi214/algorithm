n = int(input())

lst = list(map(int, input().split()))

lst.sort()

# -1을 통해 여러개 값이 도출되는 것중 가장 작은 값을 출력
print(lst[(n-1) // 2])