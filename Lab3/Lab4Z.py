d = {}
s=str(input())
res=[]
for c in s:
    if c not in d:
      res.append(c)
      d[c]=1
print ("".join(res))
