a)
n=[4,6,4,3,3,4,3,4,3,8]
i=0
a=[ ]
while i<len(n):
	j=0
	c=0
	while j<=i:
		if n[i]==n[j]:
			c+=1
		j+=1
	if c>3:
		a.append(n[i])
	i+=1
print(a)
b)
n=[4,6,4,3,3,4,3,4,6,6]
k=2
a=[ ]
while k<len(n):
	if n[k] not in a:
		a.append(n[k])
	k+=1
print(a)