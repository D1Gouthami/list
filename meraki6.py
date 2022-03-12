name=[ 'n', 'i', 't', 'i', 'n' ]
rev=name[::-1]
i=0
while i<len(name):
	if name==rev:
		i+=1
		print('haan! polindrom hai')
		break
	else:
			print('nahi! polindrom hai')