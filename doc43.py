list=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
a=4
list1=[]
while i<len(list):
	if i==a:
		list1.append(20)
		a+=4
	list1.append(list[i])
	i+=1
print(list1)