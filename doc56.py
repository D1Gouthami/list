n=[[3,4,[6],[45,6]]]
i=0
b=[ ]
while i<len(n):
	if type(n[i])==list:
		j=0
		while j<len(n[i]):
			if type(n[i][j])==list:
				k=0
				while k<len(n[i][j]):
					b.append(n[i][j][k])
					k+=1
			else:
				b.append(n[i][j])
			j+=1
	else:
			b.append(n[i])
	i+=1
print(b)
o/p:[3,4,6,45,6]
a=[[23,45,6],[23,4,5],[20,5,1]]
i=0
b=[ ]
while i<len(a):
	j=0
	c=a[i][j]
	while j<len(a[i]):
		if a[i][j]<c:
			c=a[i][j]
			b.append(c)
		j+=1
	print(c,end=' ')
	i+=1