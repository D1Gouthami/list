list=[34.67,12,-94.89,"python",0,"c#"]
i=0
b=[]
while i<len(list):
	if type(list[i])==int:
		b.append(list[i])
	i+=1
print(b)