''' Rubik's Cube Turn Notation (36 symbols; 54 when double turns (eg. R2) are included):
R  L  U  D  F  B
R' L' U' D' F' B'
r  l  u  d  f  b
r' l' u' d' f' b'
   M     E  S 
   M'    E' S'
X     Y     Z
X'    Y'    Z'

also:  R2   u2    Y2  etc.   Note: R'2 is probably always printed R2  '''

'''
print ("A Rubik's Cube has many mirror and rotational symmetries.  The human body has one line of bilateral mirror symmetry, 
and the Rubik's cube shares shares this line of symmetry. Cube algorithms, like scissors and 
\nviolins, are generally designed for right-handed people. The left hand provides stability while the right hand gets 
\nthe nimble bits. By swapping the roles of your right and left hands, 
\nyou can take any standard algorithm and convert it to a left-handed version. This program takes your old 
\nright-handed alg and converts it to a left-handed version in standard notation. The new algorithm is a 
\nmirror reflection of the original, both in terms of the action on the cubies and the turns themselves. 
\n\nPaul McCartney plays a left-handed bass.  Why shouldn't left-handed Rubik's cubers also optimize their performance 
\nby using algorithms designed for their hands? \n")
'''

'''What is a good naming convention for variables within a function?  I always want
to name them the same name as the original, but I guess that's bad.'''

'''Reflection in a mirror parallel to the R (and the L) face has the following results:
All clockwise turns are reflected to counterclockwise and vice versa, except M,X,M',X' turns, which are unchanged.T
R turns become L (in addition to changing direction- see above) and vice versa (eg. R becomes L')
r turns become l (in addition to changing direction- see above) and vice versa (eg. l becomes r') 
The 2 that indicated a double turn remains unchanged. (eg. U2 -> U2;  L2 -> R2)  '''

print ("A Rubik's Cube has the same bilateral, mirror symmetry of the human body. Cube algorithms, like scissors and \nviolins, are generally designed for right-handed people. In the case of the cube, the left hand provides stability while the right hand gets \nthe nimble bits. By swapping the roles of your right and left hands, \nyou can take any standard algorithm and convert it to a left-handed version. This program takes your old \nright-handed alg and converts it to a left-handed version in standard notation. The new algorithm is a \nmirror reflection of the original, both in terms of the action on the cubies and the turns themselves. \n\nPaul McCartney plays a left-handed bass.  Why shouldn't left-handed Rubik's cubers also optimize their performance \nby using algorithms designed for their hands? \n")

#Get input, clean it up
alg = input("Please enter an algorithm of any length: ")
alg = alg.replace("'2", "2")	# converts nonstandard notation such as R'2 to standard R2
alg = alg.replace ("x", "X")	# corrects nonstandard X,Y,Z notation
alg = alg.replace ("y", "Y")
alg = alg.replace ("z", "Z")

# Assemble data on inputed alg
alg_parity_moveable = alg.replace("'","")	# Gives length of alg in a moveable-center model: R'XU2L has length of 5
alg_parity_fixed = alg_parity_moveable.replace("X","")
alg_parity_fixed = alg_parity_fixed.replace("Y","")
alg_parity_fixed = alg_parity_fixed.replace ("Z","")	# Gives length of alg in a fixed-center model: R'XU2L has length 4
alg_char = alg_parity_moveable.replace("2", "")	# 2 and ' removed.  alg reduced to the number of turns the user experiences, with both 90 and 180 turns counted as one turn

#print (len(alg_char))
#print("")

def prime_swap(algae):	# Letters in the alg that were followed by a prime ' (indicating a counterclockwise turn) have their primes removed; Letters that had no prime ' (indicated a default clockwise turn) have a prime added to them
	for x in range(0,len(alg_char)):
		algae = algae[1:len(algae)] + algae[0]		# First character of string moved to end. This is performed with every algorithm
		if algae[-1] == "M" or algae[-1] == "X":
			if algae[0] == "2" or algae[0] == "'":
				algae = algae[1:len(algae)] + algae[0]  # First character of string moved to end
		else:	# For all [-1] characters that aren't M or X
			if algae[0] == "2":
				algae = algae[1:len(algae)] + algae[0]	# "2" moved  (from first position to end)
			elif algae[0] == "'":
				algae = algae[1:len(algae)] 	# ' deleted  (from first character position)
			else:
				algae = algae + "'"		# ' added  (to end position)
	return(algae)


#Here is an outdated function, that was never completed anyway:
#def prime_swap(algae):	# Letters in the alg that were followed by a prime ' (indicating a counterclockwise turn) have their primes removed; Letters that had no prime ' (indicated a default clockwise turn) have a prime added to them
#	for x in range(0,len(alg)):   
#		algae = algae[1:len(algae)] + algae[0]	  # First character of string removed, added to end
#		if algae[-1] != "X" and algae[-1] != "M":
#			algae = algae + "'"					  # Prime ' added to end, except in the case of X and M
#	algae = algae.replace("'''", "") 			  # Removes the inadvertant ''' that got built around each original prime (except those following X and M), thus removing all original primes 
#	algae = algae.replace ("'2'", "2")			  # Removes primes inadvertantly created around instances of 2 (indicating a double turn), ensuring that R2, u2, Y2 etc. remain unchanged
#	algae = algae.replace("''", "'")			  # Replaces '' with '.   '' will only be found in cases where prime_swap inadvertantly converted X' to X'' or M' to M''. Ensures that X,M,X', and M' are all ultimately unchanged by prime_swap
#	return(algae)


alg = prime_swap(alg)  # I'm sure this is not the right way to do this !!

# Now "R" and "L" get swapped (and also "r" and "l"), using a temporary placeholder variable  
alg = alg.replace("R","tmp")
alg = alg.replace("L", "R")
alg = alg.replace ("tmp", "L")

alg = alg.replace("r", "tmp")
alg = alg.replace("l", "r")
alg = alg.replace("tmp", "l")
		
print ("Your left-handed (mirror) algorithm is: " + alg)
