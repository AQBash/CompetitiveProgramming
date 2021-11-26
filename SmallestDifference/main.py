def smallestDifference(arrayOne, arrayTwo):
    #arrayOne.sort()
	#arrayTwo.sort()
	sol=0
	bestVal=abs(arrayOne[0]-arrayTwo[0])
	for i in arrayOne:
		for j in arrayTwo:
			currVal=abs(i-j)
			if currVal<bestVal:
				bestVal=currVal
				sol=[i,j]
    return sol
