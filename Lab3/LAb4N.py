def sum(a, b):
    if b < a:
        if b > 0:
            a += 1
            b -= 1
            sum(a, b)
        elif b < 0:
            a -= 1
            b += 1
            sum(a, b)
        elif b == 0:
            print(a)
    else:
        if a > 0:
            b += 1
            a -= 1
            sum(a, b)
        elif a < 0:
            b -= 1
            a += 1
            sum(a, b)
        elif a == 0:
            print(b)


a, b = input().split()
sum(int(a), int(b))
