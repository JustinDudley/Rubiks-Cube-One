# This module takes a Rubik's Cube algorithm, perhaps inputed by a user, and 
# converts it to a list, so that it can be manipulated by other programs as a list

def convert_to_list(alg_stri):
	# Takes a string and converts it to a list, for better functionality in manipulation by other programs.
	# This function assumes it has been given a properly cleaned up algorithm.
	
	alg_bare = alg_stri[:] # make a copy
	alg_bare = alg_bare.replace("'", "")
	alg_bare = alg_bare.replace("2", "")
	# print(alg_bare)
	
	

	alg_list = [] 		# Initialize
	alg_stri += "9" 	# Creates dummy character at end of string, so that for-loop doesn't throw error on its final loop
	for char in alg_bare:		# says how many times I'm going to need to convert a portion of the string to an item of the list	
		if alg_stri[1] == "'":
			alg_list.append(alg_stri[0] + "3")
			alg_stri = alg_stri[2:]	# first and second characters of string removed
		elif alg_stri[1] == "2":
			alg_list.append(alg_stri[0] + "2")
			alg_stri = alg_stri[2:]	# first and second characters of string removed
		else:
			alg_list.append(alg_stri[0] + "1")
			alg_stri = alg_stri[1:]	# only the first character of string removed
	return alg_list
	
	
	
# print (convert_to_list("R'UF2R"))
