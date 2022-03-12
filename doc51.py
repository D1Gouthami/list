A. 
list=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]

list1=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
a=[ ]
while i<len(list):
	b=list[i]+list1[i]
	a.append(b)
	i+=1
print(a)

Output:-[[10, 20, 61], [30, 40, 12, …
a=[5,3,3,2,7,10,6,2,2,10,1]
i=0
while i<len(a):
	j=0
	while j<len(a):
		if (a[i]<a[j]):
			a[i],a[j]=a[j],a[i]
		j+=1
	i+=1
print(a)