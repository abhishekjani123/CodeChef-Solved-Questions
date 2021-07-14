t = int(input())
x1 = 0
y1 = 0
l = 0
for i in range(t):
    x,y = input().split()
    x = int(x)
    x1 = x1 + x
    y = int(y)
    y1 = y1 + y
    if(x1>y1):
        diff = x1 - y1
        winner = 1
    else:
        diff = y1 - x1
        winner = 2
    if(diff > l):
        l = diff
        w = winner
print(w,l)
    
    
