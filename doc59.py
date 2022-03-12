a=[9,2,4,6,7,9]
i=0
b=[ ]
while i<len(a):
	x=a[i-1]+a[-i]
	b.append(x)
	i+=2
print(b)