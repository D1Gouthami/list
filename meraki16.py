elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
avg=0
avg1=0
while i<len(elements):
	if elements[i]%2==0:
		avg=avg+(elements[i])/len(elements)
	else:
		avg1=avg1+(elements[i])/len(elements)
	i+=1
print('avg of even=',avg,'avg of odd=',avg1)