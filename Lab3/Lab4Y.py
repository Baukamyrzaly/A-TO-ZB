def chess(a, b):
    c = True
    d = False
    if b % 2 == 1:
        for i in range(a):
            for j in range(b):
                if c:
                    print(1, end="")
                    c = False
                    d = True
                else:
                    print(0, end="")
                    c = True
                    d = False
            print("")
    else:
        c = False
        d = True
        for i in range(a):
            c=d
            for j in range(b):
                if c:
                    print(1, end="")
                    c = False
                    d = True
                else:
                    print(0, end="")
                    c = True
                    d = False
            print("")


a, b = input().split()
chess(int(a), int(b))
    
