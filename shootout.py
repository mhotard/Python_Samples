# Three person duel
# A has a 0.3 of hitting his man
# B has 1 chance of hitting her man
# C has a .5 chance of hitting her man
# What should A do?

living_shooters = np.array(['A', 'B', 'C'])

shooter_skill = {'A':.3, 'B':1, 'C':.5}

def death(person):
	global living_shooters
	living_shooters = living_shooters[living_shooters != person]
	


def shot_result(shooter, target):

	chance = shooter_skill[shooter]
	print '%s aims and fires at %s' % (shooter, target)
	#print 'He has a %f chance of hitting him' % chance
	#print shooter
	#print target

	if(np.random.binomial(1, chance)):
		print '%s kills %s \n' % (shooter, target)
		death(target)
	else: 
		print '%s misses %s \n' % (shooter, target)



A_always = raw_input('Who should Alan shoot? ')

#running lots of times to get an idea of success
trials = 100
success = [0] * trials

for i in range(0, trials):

	A_choice = A_always

	#sets the living shooters
	living_shooters = np.array(['A', 'B', 'C'])

	#runs while A is alive
	while 'A' in living_shooters and (len(living_shooters) > 1):
		print '---------------------------------------'
		print 'Round %d' % i
		#A_choice = raw_input('Who should Alan shoot? ')
		#checks to see if A's target is alive
		while (A_choice in living_shooters) == False:
			A_choice = raw_input('Target down. Choose another target. ')
		shot_result('A', A_choice)
		# B and C get their turns if they are alive
		# they pick a random target from living shooters not themselves
		if 'B' in living_shooters:
			shot_result('B', np.random.choice(living_shooters[living_shooters != 'B'], 1)[0])
		if 'C' in living_shooters:
			shot_result('C', np.random.choice(living_shooters[living_shooters != 'C'],1)[0])

	#while loops exit if A dies or one shooter left
	#presents these results
	if 'A' in living_shooters:
		print 'Nice shooting, A! You got them all.'
		success[i] = 1
	else:
		print 'Better luck next time. You are dead.'
		success[i] = 0

sum(success)


