def getNthFib(n):
    if n <=2:
		return n-1
	else:
		return getNthFib(n-1)+getNthFib(n-2)
