def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


a,b = input().split()
a=int(a)
b=int(b)
e = gcd(a,b)+lcm(a,b)
print(e)
