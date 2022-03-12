char = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
m=[]
while i<len(char):
    count=0
    n=[]
    j=0
    while j<len(char):
        if char[i]==char[j]:
            count=count+1
        j=j+1
    n.append(char[i])
    n.append(count)
    if n not in m:
        m.append(n)
    i=i+1
print(m)
 