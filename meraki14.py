number=30
n=[10,11,12,13,14,17,18,19]
i=0
l1= []
while i<len(n):
	l2=[]
	j=i
	while j<len(n):
		if n[i]+n[j]==30:
		    l2.append(n[j])
		    l2.append(n[i])
		    l1.append(l2)
		j+=1
	i+=1
print(l1)