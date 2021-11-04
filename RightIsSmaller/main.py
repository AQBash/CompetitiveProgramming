def rightSmallerThan(array):
    cnt=0
	outputArray=[]
	for idx, i in enumerate(array):
		for j in array[idx:]:
			if j<i:
				cnt+=1
    	outputArray.append(cnt)
		cnt=0
	return outputArray
