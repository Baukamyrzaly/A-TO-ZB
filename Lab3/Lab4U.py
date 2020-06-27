

def lino(a, b, x, y):
    if x + y - a - b >=0:
        print("Thanks, Nurbek")
    else:
        print("Impossible")


a, b, x, y = input().split()
a = int(a)
b = int(b)
x = int(x)
y = int(y)

lino(a, b, x, y)
