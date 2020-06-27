even = 0
odd = 0
a = input().split()
for i in range(len(a) - 1):
    if int(a[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
print("%f" % int(even * 100 / (len(a) - 1)) + "%" + " " + "%f" % int(odd * 100 / (len(a) - 1)) + "%")
