prime=[]
def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if (x % y)==0:
                return False
    else:
        return False
    return True
l=range(1,101)
for i in l:
    if(is_prime(i)):
        prime.append(i)
print(prime)

