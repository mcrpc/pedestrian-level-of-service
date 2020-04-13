def PLOS(sidewalk, lane, spd):
	y=0
	if spd <=25:
		if lane ==2:
			if sidewalk ==2:
				y=1
			elif sidewalk ==1:
				y=2
			else:
				y==2
		elif lane >2:
			if sidewalk ==2:
				y=1
			elif sidewalk ==1:
				y=3
			else:
				y==3
	elif spd >25 and spd <40:
		if lane ==2:	
			if sidewalk == 2:
				y=2
			elif sidewalk == 1:
				y=3
			else:
				y=4
		elif lane >2:
			if sidewalk ==2:
				y=3
			elif sidewalk ==1:
				y=4
			else:
				y=5
	elif spd >=40:
		if lane == 2:
			if sidewalk ==2:
				y=3
			elif sidewalk ==1:
				y= 4
			else:
				y=5
		elif lane >2:
			if sidewalk ==2:
				y=4
			elif sidewalk ==1:
				y=5
			else:
				y=5
	return y
