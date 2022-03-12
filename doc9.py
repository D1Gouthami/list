numbers=[50,40,23,70,56,12,5,7,10]
i=0
a=0
while i<len(numbers):
	if numbers[i]>a:
		a=numbers[i]
	i+=1
j=0
max2=0
while j<len(numbers):
		if numbers[j]<a:
			if numbers[j]>max2:
				max2=numbers[j]
		j+=1
k=0
max3=0
while k<len(numbers):
	    if numbers[k]<max2:
	    	if numbers[k]>max3:
	    		max3=numbers[k]
	    k+=1	    
print(a)
print(max2)
print(max3)