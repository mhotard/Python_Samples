#Probabily of rolling a six given X number of dice
#Answers the question of whehter or not more dice is better
#More dice is actually worse

import numpy as np

#much faster to do this with a binomial
def roll_dice2(dice_number, sixes_needed, trials):
	chance = float(1)/float(6)
	#dice number is trials, change is 1/6, then how many times
	#add up the times you get the sixes you need
	success = sum(np.random.binomial(dice_number, chance, trials) >= (sixes_needed))
	print success
	return float(success)/float(trials)

def roll_dice(dice_number, sixes_needed, trials):
	success = Series([0] * trials)
	# loops through trials number of times rolling dice and checking
	for i in range(0, trials):
		roll = Series(np.random.choice(range(1,7), dice_number, replace=True))
		#print roll
		counts = roll.value_counts()
		#print counts
		if 6 in roll.value_counts():
			#print ('Six found!')
			if roll.value_counts()[6] >= sixes_needed:
				success[i] = 1
				#print ('Success! /n')

	return success

dice_num = int(raw_input('Dice to roll: '))

six_needed = int(raw_input('How many sixes do you need?' ))

trial_runs = 1000

#answer = roll_dice(dice_num, six_needed, trial_runs)

#print answer.mean()


answer2 = roll_dice2(dice_num, six_needed, trial_runs)
print 'You will win %f percent of the time' % (round(answer2, 2) * 100)

