t = int(input())
a = []
for i in range(t):
    x = int(input())
    a.append(x)

a.sort()  # In this way time doesnot exceed
# sorting(a)

for i in range(len(a)):
    print(a[i])

# In this way time limit exceeds (any suggestion)
# def sorting(a):            
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if(a[i] > a[j]):
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
#     for i in range(len(a)):
#         print(a[i])

