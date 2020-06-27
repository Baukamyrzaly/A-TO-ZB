def point(x1, y1, x2, y2, x3, y3):
    if (x1 <= x3 <= x2) and (y2 <= y3 <= y1) :
        print("yes")
    else:
        print("no")


x1, y1, x2, y2, x3, y3 = input().split()
point(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
