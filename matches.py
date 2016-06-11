#Probabily question
#Given M men and W women randmonly sitting in a row
#How many oppistite sex couples will be formed

import numpy as np

#Input for men and women

men = int(raw_input('Men: '))

women = int(raw_input('Women '))

#concatenating into a group
group = ['M'] * men + ['W'] * women

trials = 100000


match = Series([0] * trials)

#going to run this trials times
for j in range(0, trials):
	#creates our random seating pattern
	seats = np.random.choice(group, len(group), replace=False)

	#goes through each two person pair and sees if they match
	for i in range(0,(len(seats)-1)):
		#if oppisite, then they match
		if (seats[i] != seats[i+1]):
			match[j] = match[j] + 1
			#print "Match found with seats ", i, " and ", i + 1
		#else:
			#print "No match found with seats ", i, " and ", i + 1

print match.mean()