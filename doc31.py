A .

list=[-4,-3,-2,-1,0,1,2,3,4,5]
i=0
while i<len(list):
	if -4<=list[i]<5:
		if list[i]<0:
			print(list[i],end=" ")
	i+=1

O/p:[-4,-3,-2,-1]


B.

list=[-3,-2,-1,0,1,2,3,4,]
i=0
while i<len(list):
	if -3<=list[i]<5:
		if list[i]<0:
			print(list[i],end=" ")
	i+=1