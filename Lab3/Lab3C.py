l, r = input().split()
a = []
for i in range(int(l), int(r) + 1):
    if i % 7 == 1:
        a.append(str(i)+" ")
    elif i % 7 == 2:
        a.append(str(i)+" ")
    elif i % 7 == 5:
        a.append(str(i)+" ")
print("".join(a))

