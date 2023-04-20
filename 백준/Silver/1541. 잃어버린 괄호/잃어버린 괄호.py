data = input()

# 최솟값 만들기 ( - 뒤의 값을 크게 만들어주면 최솟값이 된다.)
data =  data.split('-')
if len(data) > 1:
    val = sum(list(map(int, (data[0].split('+')))))
    for i in range(1, len(data)):
        tmp = list(map(int, data[i].split('+')))
        val -= sum(tmp)
    print(val)
else:
    data = list(map(int, data[0].split('+')))
    print(sum(data))