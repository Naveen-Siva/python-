n=int(raw_input())
k=int(raw_input())
sum=0
s=[]
for b in range(n):
    s.append(b+1)
for a in range(k):
    sum=sum+s[a]
print(sum)
