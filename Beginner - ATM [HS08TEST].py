x,y = input().split()
x = int(x)
y = float(y)
if(x%5 == 0 and x+0.50<=y):
    x = x+0.50
    t = y-x
    print('%0.2f' %t)
else:
    print('%0.2f' %y)