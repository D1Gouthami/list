a=int(input('num'))
i=1
while i<=a:
	j=1
	b=[ ]
	while j<=10:
		d=i*j
		b.append(d)
		j+=1
	print(i,',',b,',',end=' ')
	i+=1