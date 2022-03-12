a=['red','maroon','yellow','white']
i=0
b=[ ]
while i<len(a):
	j=0
	m=[ ]
	while j<len(a[i]):
		m.append(a[i][j])
		j+=1
	i+=1
	b.append(m)
print(b)