n=input()
a=[int(x) for x in input().split()]
b=int(input())
sum = 0
for i in a:
    if i >= b:
        sum +=1
print(sum)
