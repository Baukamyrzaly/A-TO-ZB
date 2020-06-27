def fav(n):
    a = []
    sum = 0
    while n != 0:
        a.append(n % 10)
        n = int(n / 10)
    for i in a:
        sum += i
    if sum % a[0] == 0:
        print("Yes")
    else:
        print("No")


n = input().strip()
fav(int(n))

