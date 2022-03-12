elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]  
i=0
a=[ ]
b=[ ]
c=0
c1=0
sum=0
sum1=0
avg=0
avg1=0
while i<len(elements):
	if elements [i]%2==0:
	   a.append(elements[i])
	   sum=sum+(elements[i])
	   avg=avg+(elements[i])/len(elements)
	   c+=1
	else:
		a.append(elements[i])
		sum1=sum1+(elements[i])
		avg1=avg1+(elements[i])/len(elements)
		c1+=1
	i+=1
		
print('len of the elements',len(elements))
print('c of even=',c)
print('c of odd=',c1)
print('sum of even=',sum)
print('sum of odd=',sum1)
print('sum of even and odd=',sum+sum1)
print('avg of even=',avg)
print('avg of odd=',avg1)