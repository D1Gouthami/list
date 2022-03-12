a=[1,2,3,4,5,6,7,8,9,10]
i=0
odd=[]
even=[]
even_prime=[]
odd_prime=[]
while i<len(a):
	if a[i]%2==0:
		even.append(a[i])
		if a[i]==2:
			even_prime.append(2)
	else:
		odd.append(a[i])
		j=2
		while j<a[i]:
			if a[i]%j==0:
				break
			else:
				j+=1
		if a[i]==j:
			odd_prime.append(a[i])
	i+=1
print("odd list is ",odd)
print("odd prime list is" ,odd_prime);
print("even list is ",even);
print("even prime lsit is ",even_prime);
