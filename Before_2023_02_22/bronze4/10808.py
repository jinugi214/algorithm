import sys
import string

input = sys.stdin.readline

s = input().rstrip()

data = [0] * len(string.ascii_lowercase)

for i in s:
    data[ord(i) - ord('a')] += 1

print(*data)