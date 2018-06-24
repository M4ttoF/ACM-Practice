#Tri
#Matthew Farias

def swap(a, b):
	c=a
	a=b
	b=c

def line(a1,a2,a3,sign):
	return str(a1)+sign+str(a2)+'='+str(a3)

def tri(n1, n2, n3):
	n1=int(n1)
	n2=int(n2)
	n3=int(n3)
	if n2>n1:
		swap(n1,n2)

	if n1==n3:
		if n2==0:
			return line(n1,n2,n3,'+')
		else:
			return line(n1,n2,n3,'*')
	if n1>n3:
		if (n1-n3)==n2:
			return line(n1,n2,n3,'-')
		else:
			return line(n1,n2,n3,'-')
	else:
		if (n3-n1)==n2:
			return line(n1,n2,n3,'+')
		else:
			return line(n1,n2,n3,'*')
while True:
	inp = input()
	if inp=="":
		break
	arr=inp.split()
	print(tri(arr[0],arr[1],arr[2]))
