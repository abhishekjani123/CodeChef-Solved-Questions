n = int(input())
a = list(map(int,input().split()))[:n]
odd_count=0
even_count=0
for i in range(n):
    if(a[i]%2==0):
        even_count += 1
    else:
        odd_count += 1
if(even_count > odd_count):
    print("READY FOR BATTLE")
else:
    print("NOT READY")