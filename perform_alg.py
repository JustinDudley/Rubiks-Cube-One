
'''The 54 notated Rubik's Cube turns can be grouped in various ways. In this program (well, really in the module that this program calls), they are first 
grouped into 3 sets of 6, based on whether they turn around the X-axis, Y-axis, or Z-axis. Then, each of these 18 turns can be iterated 1x, 2x, or 3x to 
create all 54 possibilities.  In the future, I may want to write out lists for each of the 54 turns, to shorten runtime.  '''

'''A CONFIGURATION is represented by a dense list of 54 numbers, each number corresponding to one sticker on the cube.
variables representing static configurations are **lists of 54 letters**, each letter corresponding to one sticker on the cube. Their names end in _cfg
variables representing turns (= sequences, = algoritms) are **tuples of 54 numbers**, and their names end in  _trn
It can be extraordinairily difficult to tease out configurations from turns in your mind, so beware.   '''


# Edge stickers make up the first 24 numbers of a list or tuple; corner stickers make up the second 24. Center pieces make up the final 6.
# Letter assignment method is borrowed from the Old Pochmann system of blindfolded cube solving.
# Future possibilities include using a truncated list of 20 items, corresponding to just one sticker from each cubie, then 
# running a special "decompress" function after running the turn alg.

# Usually I will want to start with a solved cube configuration.  Ultimately, I would like to be able to start
# with different configurations, and ultimately I would like this program to be able to draw starting configurations from a library/file'
# and also store resultant configurations in a file.  Ultimately, different users could have their own files.



from turns import take_turns
from string_to_list import convert_to_list

# The following list bridges the gap, in a way I don't completely understand, between (1) algs, expressed as tuples with 
# numbers, and (2) configs, expressed as lists with letters.
# This list is used to derive new sequence tuples.  A sequence could be a single turn, eg. R', or it could be a whole alg, eg. RUR'F
# This list has been used to derive all 18 of the programs turns from a small few
derive_seqtuple_list =[0,1,2,3,  4,5,6,7,  8,9,10,11,  12,13,14,15,  16,17,18,19,  20,21,22,23,    24,25,26,27,  28,29,30,31,  32,33,34,35,  36,37,38,39,  40,41,42,43,  44,45,46,47,    48,49,50,51,52,53]

# This list represents a solved cube
solvd_cfg = ['a','b','c','d',  'e','f','g','h',  'i','j','k','l',  'm','n','o','p',  'q','r','s','t',  'u','v','w','x',    'a','b','c','d',  'e','f','g','h',  'i','j','k','l',  'm','n','o','p',  'q','r','s','t',  'u','v','w','x',    'a','e','i','m','q','u']

#  need to comment-out 2 of 3 variable definitions below
#start_cfg = derive_seqtuple_list[:]		# Use this to create/test new tuples for new sequences, such as M,Z, and f, or longer too
start_cfg = solvd_cfg[:]					# The standard way to test the effect of an algorithm on a solved cube
#start_cfg = input("Please enter a configuration you would like to see the results for. \n(Spoiler alert:  Good luck! Because at this point of my progress with this program, you now need to enter a 48-number list!!):  ")


#  need to comment-out 1 of 2 variable definitions below
#user_stri = "URU'R2"	# coder chooses an algorithm to test
user_stri = input("Please enter the letters of your algorithm (eg. RUR'...): ")


user_list = convert_to_list(user_stri)	# call imported module to convert string to list
new_cfg = start_cfg[:]	# make copy of start configuration for use in function
for i in range (0, len(user_list)):		# For each, separate, turn in user's algorithm:
	# The three arguments passed to the function "take_turns" are:  (1) a letter, such as R or U, (2) the number of iterations the function should 
	# use, specifically: 1 for a clockwise turn, 2 for a double turn, and 3 for an anti-clockwise turn, and (3) the initial cube configuration, usually
	# the solved configuration.
	new_cfg = take_turns(user_list[i][0], int(user_list[i][1]), new_cfg)

print ("\n Your starting configuration was: \n" + str(start_cfg))
print ("\n The algorithm you wished to test was: \n" + str(user_stri))
print ("\n The resultant configuration is: \n" + str(new_cfg))



''' 
Create s dictionary with configs?  {start_config: [abcd...]} ??
Hmmm-  ideally this would be in a FILE.  Could it be a file that was built to look like a dictionary, so that when I read from the file, it
came into my script in the form of a dictionary?  Or could be easily converted to a dictionary?
'''

'''
Dictionaries can contain FUNCTIONS as values.  So, eventually I could have user input such as "mirror" and that input would 
access a function inside a dictionary directly.  There could be a menu of options for users to select actions, each menu item corresponding
to a key:value pair
'''

'''
Things to ask user:
Do you want to start with a solved configuration?  Or do you have something else in mind?  Would you like to choose from a menu?"
What is your algorithm that you want tested?
Would you like to see the mirror image of your algorithm?
Would you like to see a mirror image of your starting configuration?

Definitions to print somewhere for user to read:
Configuration:  A **static** report, using 54 stickers. 
Manipulation:  (?)  a **dynamic** plan to move these 54 stickers.  Looks like a config, but isn't.  Expressed with 54 numbers.
'''
