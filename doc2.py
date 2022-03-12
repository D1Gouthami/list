a=[['g','f','g',],['i','s'],['b','e','s','t']]
b=['g','f','g']
c=['i','s']
d=['b','e','s','t']
d=b+c+d
i=0
while i<len(d):
   print(d[i],end='')
   i+=1


   a=[6,1,3,5,6,3,1]
i=0
b=[ ]
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
		d=b[i]*i*i+a[i]*i
	i+=1
print(d)