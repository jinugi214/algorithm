import sys

input = sys.stdin.readline

N = input()

data = list(input().split())

M = input()

check_data = list(input().split())

dict = {}

for val in data:
    dict.setdefault(val, 1)

for val in check_data:
    if dict.get(val) is None:
        print(0)
    elif dict[val] == 1:
        print(1)