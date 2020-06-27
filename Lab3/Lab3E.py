a = []


def push(n):
    a.append(n)
    print("OK")


def size():
    print(len(a))


def back():
    print(a[len(a) - 1])


def front():
    print(a[0])


def pop():
    a.pop()
    print("OK")


def clear():
    a.clear()
    print("OK")


while True:
    s = input().split()
    if s[0] == "push":
        n = int(s[1])
        push(n)
    elif s[0] == "size":
        size()
    elif s[0] == "end":
        print("Black Devil")
        break
    elif s[0] == "back":
        back()
    elif s[0] == "front":
        front()
    elif s[0] == "pop":
        pop()
    elif s[0] == "clear":
        clear()

