number=[50,40,23,12,5,10,7]
i=0
c=0
while i<len(number):
	if 20<=number[i]<=40:
		c+=1
	i+=1
print(c)