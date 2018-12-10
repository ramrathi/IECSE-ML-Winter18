n=101
[x for x in range(n)]
//prints numbers from 0 to 100
lprime=[]
for i in range (2,n):
   if(n%i)==0:
   break

else:
lprime.append(n)

print lprime

