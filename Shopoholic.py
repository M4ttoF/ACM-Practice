#Shopoholic
#Matthew Farias

n = int(input())
arr = sorted(input().split(),reverse = True)
pos=2
savings=0
while(pos<n):
	savings+= int(arr[pos])
	pos+=3
print(savings)
