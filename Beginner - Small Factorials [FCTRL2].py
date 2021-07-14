t = int(input())
for i in range(t):
    x = int(input())
    ans = 1
    while(x>0):
        ans = ans*x
        x = x-1
    print(ans)