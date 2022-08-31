import sys
import string

input = sys.stdin.readline

word = input().rstrip()

for x in word:
    if x in string.ascii_lowercase:
        if ord('z') < (ord(x) + 13):
            new_x = ord('a') + (ord(x) + 13 - ord('z')) - 1
            print(chr(new_x), end="")
        else:
            print(chr(ord(x) + 13), end="")
    elif x in string.ascii_uppercase:
        if ord('Z') < (ord(x) + 13):
            new_x = ord('A') + (ord(x) + 13 - ord('Z')) - 1
            print(chr(new_x), end="")
        else:
            print(chr(ord(x) + 13), end="")
    elif x in string.digits:
        print(x, end="")
    elif x == " ":
        print(" ", end="")