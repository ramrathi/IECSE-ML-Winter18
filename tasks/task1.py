a = 32
b = 5
c = 7
d = 10

largest = -2147483648
secondLargest = -2147483648

if a > largest:
	secondLargest = largest
	largest = a
elif a > secondLargest and a != largest:
	secondLargest = a

if b > largest:
	secondLargest = largest
	largest = b;
elif b > secondLargest and b != largest:
	secondLargest = b


if c > largest:
	secondLargest = largest
	largest = c
elif c > secondLargest and c != largest:
	secondLargest = c

if d > largest:
	secondLargest = largest
	largest = d
elif d > secondLargest and d != largest:
	secondLargest = d

print("The second largest - {}".format(secondLargest))
