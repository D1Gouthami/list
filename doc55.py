list=[[3,4,5,],[5,6,7],[1,2,3]]
a=1
b=2
i=0
j=0
d=[ ]
while j<len(list):
	c=list[i][j]+list[a][j]+list[b][j]
	d.append(c)
	j+=1
print(d)