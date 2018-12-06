l = range(1,101)

prime_l = []


for i in range(1,100):
	prime = 1
	for j in range(2,(l[i]//2) + 1):
		if l[i] % j == 0:
			prime = 0

	if prime == 1:
		prime_l.append(l[i])

print("The prime list is {}".format(prime_l))		

print('The alternate indexed prime list is')

for i in range(0,len(prime_l) + 1, 2):
	print(prime_l[i])