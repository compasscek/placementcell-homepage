x=10
y=1
height=[11,10,10,9]
n=len(height)
jumps=0
for i in range(n):
    if height[i]<= x:
        jumps+=1
        continue
    h = height[i]
    while(h>x):
        jumps+=1
        h = h-(x-y)
        jumps+=1
        print(jumps)