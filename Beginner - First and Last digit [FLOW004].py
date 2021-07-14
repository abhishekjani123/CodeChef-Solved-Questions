t = int(input())
for i in range(t):
    x = input()
    res = list(map(int,x))
    length = len(res)
    result = res[0] + res[length-1]
    print(result)