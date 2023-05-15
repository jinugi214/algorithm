from collections import deque

s, t = map(int, input().split())

rlt = []


def bfs():
    q = deque()
    q.append((s, ''))
    did = set()
    while q:
        val, op = q.popleft()
        if val in did:
            continue
        else:
            did.add(val)
        if val > 10 ** 9 or val < 1:
            continue
        if val == t:
            rlt.append(op)
            return

        q.append((val * val, op + '*'))
        q.append((val + val, op + '+'))
        q.append((val - val, op + '-'))
        if val != 0:
            q.append((val / val, op + '/'))


if s == t:
    print(0)
else:
    bfs()
    if rlt:
        print(rlt[0])
    else:
        print(-1)
