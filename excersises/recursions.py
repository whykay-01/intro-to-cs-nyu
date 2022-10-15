
					######
'''import time

values = {}
def fibonacci(number):

	if number == 0:
		return 0

	if number == 1:
		return 1

	if number not in values:
		values[number] = fibonacci(number-1) + fibonacci(number-2)
	return values[number]
	
start = time.time()
print(fibonacci(200))
end = time.time()
print(end-start)'''
					######
'''def sum_of_n(n):
	if n == 1:
		return 1

	return sum_of_n(n-1) + n

print(sum_of_n(100))'''

					######

'''def power(x, n):
	if n == 0:
		return 1
	return x * power(x, n-1)

print(power(2, 3))'''

					######

empty = []

def reverse_list(x):
	if len(x) == 0:
		return []
	# empty.append(reverse_list(x).pop)
	# return empty
	return [x[-1]] + reverse_list(x[:-1])

my_list = [1,2,3,4]
print(reverse_list(my_list))





