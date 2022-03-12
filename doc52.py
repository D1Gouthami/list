a=[" pr iya"," lax m i","hi ma bin du"]
i=0
space=[ ]
while i<len(a):
	j=0
	st=' '
	while j<len(a[i]):
		if a[i][j]!=' ':
			st+=a[i][j]
		j+=1
	space.append(st)
	i+=1
print(space)