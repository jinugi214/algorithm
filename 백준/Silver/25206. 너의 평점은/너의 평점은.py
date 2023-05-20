val = 0
cnt = 0
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값

grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0' : 1.0, 'F' : 0.0}

for _ in range(20):
    data = list(input().split())
    if data[2] == 'P':
        continue
    else:
        val += float(data[1]) * grade_dict[data[2]]
        cnt += float(data[1])
try:
    print(format(val / cnt, ".6f"))
except(ZeroDivisionError):
    print(format(0, ".6f"))