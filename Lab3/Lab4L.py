def isBacktoHome(moves):
    a = [0, 0]
    for i in range(len(moves)):
        if moves[i] == "U":
            a[1] += 1
        elif moves[i] == "D":
            a[1] -= 1
        elif moves[i] == "R":
            a[0] += 1
        elif moves[i] == "L":
            a[0] -= 1

    if a[0] == 0 and a[1] == 0:
        return True
    return False


s = input()
if isBacktoHome(s):
    print("True")
else:
    print("False")
