x, y, w, h = map(int, input().split())

val = []

val.append(x)
val.append(y)
val.append(abs(w-x))
val.append(abs(y-h))

print(min(val))
