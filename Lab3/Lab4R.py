def who(num):
    i = 1
    whos = True
    while num > 0:
        num -= i
        whos = True
        if num > 0:
            num -= 2 * i
            whos = False
        i += 1
    return whos


n = int(input())
if who(n):
    print("Bob")
else:
    print("Nelson")
