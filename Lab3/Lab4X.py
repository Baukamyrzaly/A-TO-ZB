a = []


def toSev(num):
    if num > 7:
        a.append(num % 7)
        toSev(int((num - num % 7) / 7))
    elif num==7:
        print(int(10))
    else:
        a.append(num)


n = int(input())
toSev(n)
b = [str(i) for i in a]
b.reverse()
print("".join(b))

