t = int(input())
for i in range(t):
    x = int(input()) #447474
    count = 0
    while(x>0):
        num = x%10
        if(num == 4):
            count = count+1
        x = x//10
    print(count)
