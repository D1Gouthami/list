a=[[3,5,67],[3,5,45],[5,67,28]]
i=0
b=[ ]
while i<len(a):
	j=0
	c=a[i][j]
	while j<len(a[i]):
		if a[i][j]>c:
			c=a[i][j]
			b.append(c)
		j+=1
	print(c,end=' ')
	i+=1