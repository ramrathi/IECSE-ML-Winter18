l1=[]
l2=[]

for i in range(1,101):
  l1.append(i)

for i in l1:
  flag=0

  if i!=1:
    for j in range(2,(i/2)):
        if i%j==0:
            flag=1
            break
    if flag==0:
        l2.append(i)

for i in range(0,len(l2),2):
  print l2[i]
