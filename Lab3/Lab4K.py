def climb(scores, k):
    for i in scores:
        if (int(i[0]) + int(i[1]) + int(i[2]))/3 >= int(k):
            return True
    return False

n,k=input().split()
a=[]
for i in range(int(n)):
    row=input().split()
    for j in range(3):
        row[j]=int(row[j])
    a.append(row)
if climb(a,k):
    print("YES")
else:
    print("NO")
