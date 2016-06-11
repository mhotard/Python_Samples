import random

def roll():
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	
	return die1 +die2



instant_win = [7,11]
instant_lose = [2,3,12]

repeat = 1000000
win = []

for i in range(0,repeat):
	turn = True
	point = False
	point_val = 0
	
	while turn == True:
		total = roll()
	
		if point == False:
			if(total in instant_win):
				win.append(1)
				turn = False
			elif(total in instant_lose):
				win.append(0)
				turn = False
			else:
				point = True
				point_val = total
		else:			
			total = roll()
			if total == 7:
				win.append(0)
				turn = False
			if total == point_val:
				win.append(1)
				turn = False
	
	if i % 100 == 0: print i
						

sum(win)
			
						
		
			