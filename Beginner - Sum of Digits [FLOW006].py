t = int(input())
for i in range(t):
    x = int(input())
    sum = 0
    while(x>0):
        num = x%10
        sum = sum + num
        x = x//10
    print(sum)

    