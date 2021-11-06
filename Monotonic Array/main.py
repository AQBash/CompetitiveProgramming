def isMonotonic(array):
	diff = 0
	init = True
	LengthArray = len(array)
	if LengthArray < 2:
		return True
    
	for idx, i in enumerate(array):
		diff = array[idx+1] - array[idx]
		if diff !=0:
			if init==True:
				Initdirection = diff/abs(diff)
				init = False
			direction = diff/abs(diff)
			if direction!=Initdirection:
				return False
		if idx==len(array)-2:
			return True
			
		
