a,b = map(int, input().split())
count = 0
for i in range(a):
    x = int(input())
    if(x%b == 0):
        count = count+1
print(count)