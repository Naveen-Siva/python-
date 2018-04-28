a=int(raw_input())
aw=a
pal=0
digit=0
while(a/10<>0):
	digit+=1
	a=a/10
digit+=1
a=aw
while(digit<>0):
	digit-=1
	pal+=(aw%10)*(pow(10,digit))
	aw=aw/10
if(a==pal):
	print("yes")
else:
	print("no")


	
	
