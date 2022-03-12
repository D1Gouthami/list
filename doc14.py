a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
count=0
max=[ ]
while i<len(a):
	if a[i]>max:
		max=a[i]
		count+=1
	i+=1
j=0
count1=0
min=a[j]
while j<len(a):
	if a[j]>max:
		min=a[j]
		count1+=1
	j+=1
print((len(max),max))
print((len(min),min))
