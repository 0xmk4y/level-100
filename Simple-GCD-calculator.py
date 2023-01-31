num1= 31

num2 = 4

array = []



r = num1 % num2

while (r != 0):

	array.append(r)	num1 = num2

	num2 = r

	r = num1 % num2

	

print(array[-1])

		

	
