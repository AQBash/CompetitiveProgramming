def moveElementToEnd(array, toMove):
	lengthArray=len(array)
	limit=lengthArray
	idx=0
	limitidx=limit-1
	for idx, i in enumerate(array[:limit]):
		while array[limitidx]==toMove:
			limitidx-=1
			if limitidx==0:
				return array
		if idx>=limitidx:
			break
		else:
			if array[idx]==toMove:		
				intermediateVar=array[idx]
				array[idx]=array[limitidx]
				array[limitidx]=intermediateVar
				limitidx-=1
				idx+=1
			limit=limitidx+1
	return array
		
			
