n=[[4,5,[6],8,9,[23]]]
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
i=0
sum=0
while i<len(b):
		sum=sum+b[i]
		i+=1
print(sum)
