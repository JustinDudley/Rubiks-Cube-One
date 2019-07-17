## Rubik's Cube One

These 4 files represent my first shot ("One") at letting a user manipulate the cube with a keyboard.
There are **not yet any graphics**, and it features a **primitive user interface**, 
but **_the basic functionality is sound_**, and there is some good commented-in explanation of 
basic cube concepts.

**perform_alg.py** is the essential file.  It calls string_to_list.py and turns.py.
The user is asked to input an "algorithm", or sequence of turns, 
such as RFR' (Right face, Front face, Right face counterclockwise).  The program, which assumes we are 
starting with a solved cube, renders the result of the user's algorithm. --except that the 
configuration is a list of 54 numbers instead of a graphic, so it's not exactly user-friendly - **YET**.  

**string_to_list.py** converts the user's algorithm (a string of letters) to a list variable.

**turns.py** is the heart of the program.  It defines 18 tuples, one for each possible cube turn (R = Right, U = Up, etc.), 
and contains a function that applies the tuple to an existing configuration, re-building a new configuration element by element. 

**Cube_LH** is a fun add-on program for **left-handed** cubers.  The user enters an algorithm (perhaps taken from a website or book),
and the program generates a left-handed version of the algorithm, which, on the cube, has a mirror-image effect to the original. 
This program uses basic string manipulation techniques.

	**_Have fun, and stay tuned for more functionality!!_**