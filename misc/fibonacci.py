def fib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1

	n_2 = 0
	n_1 = 1
	current = 1
	i = 2
	while i < n:
		current = n_2 + n_1
		n_2 = n_1
		n_1 = current
		i += 1

	return current


# 0 1 1 2 3 5 8 13 21 34 55

print(fib(3))
print(fib(5))
print(fib(7))
print(fib(9))
print(fib(11))