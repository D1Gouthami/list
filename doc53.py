a=[[3,4],[6,7,[8]]]
i=0
b=[ ]
while i<len(a):
	if type(a[i])==list:
		j=0
		while j<len(a[i]):
			if type(a[i][j])==list:
				k=0
				while k<len(a[i][j]):
					b.append(a[i][j][k])
					k+=1
			else:
				b.append(a[i][j])
			j+=1
	else:
		b.append(a[i])
	i+=1
print(b)
i=0
s=0
while i<len(b):
	s=s+b[i]
	i+=1
print(s)
