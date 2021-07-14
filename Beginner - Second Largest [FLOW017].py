t = int(input())


for i in range(t):
    # First Method:
    a,b,c = map(int,input().split())
    if(a>b):
        if(b>c):
            print(b)
        else:
            if(a>c):
                print(c)
            else:
                print(a)
    elif(b>a):
        if(a>c):
            print(a)
        else:
            if(b>c):
                print(c)
            else:
                print(b)
  
    # Second Method:
    # l = list(map(int,input().split()))
    # l.sort()
    # print(l[1])
    