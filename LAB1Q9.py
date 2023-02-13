def squaresum(n) :
	sum = 0
	for i in range(1, n+1) :
		sum = sum + (i * i)
	return sum
print("Enter the number: ")
num=int(input())
print(squaresum(num))

