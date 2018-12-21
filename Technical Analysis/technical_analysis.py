# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#																		  		  #
#     The file starts the technical analysis code with different options	      #
# 	  such as searching pattern, guessing, pattern specific.				      #
#     This file imports methods from pattern_library.py, options.py, clean.py     #
# 															                      #
#																	              #
#/////////////////////////////////////////////////////////////////////////////////#



from pattern.pattern_library import load_patterns, save_patterns, create_pattern, delete_pattern, display_pattern				#importing pattern list update methods
from options.options import technical_analysis, guessing  																		#importing pattern search methods
from formatcheck.clean import clear																									#import clearing terminal method
from pattern.Class.Pattern import Pattern

import numpy as np                                          															#Matrix and nd-Array library
import pandas as pd                                         															#Dataframe library



def start_technical_analysis(data, R, bump_factor, OHLCV):
	#data = we've used 'SPY' data existing in './' directory
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}

	patterns_list = load_patterns('pattern/Class/patterns.pkl')
	#pattern list is created by adding patterns stored in a binary file

	while(1):
	#while we do not choose to exit the code
		
		#clear()
		#clear the termninal screen #just for formating
		
		option_selected = eval(raw_input('\n\tCHOOSE OPTION: \n\n\t\t1. Technical Analysis \n\t\t2. Guess \n\t\t3. Pattern Info \n\t\t4. Add Pattern \n\t\t5. Save \n\t\t6. Delete \n\t\t7. Exit\n\n'))
		
		if option_selected == 1:
		#it starts the technical pattern search for the selected pattern  #output the list of patterns found 
		#let the user choose the pattern according to date and year
			
			technical_analysis(data=data, R=R, patterns_list=patterns_list, OHLCV=OHLCV)

		if option_selected == 2:
		#it checks for the existence of given pattern ending at the mentioned date
			
			guessing(data=data, patterns_list=patterns_list, bump_factor=bump_factor, OHLCV=OHLCV, R=R)

		if option_selected == 3:
		#it displays the information of selected pattern
			
			display_pattern(patterns_list)

		if option_selected == 4:
		#it creates new pattern and add them to the pattern list
		#but remember to choose 'SAVE' after creating a pattern, to add it to pattern library
			
			patterns_list.append(create_pattern())

		if option_selected == 5:
		#it updates the pattern library file 
			
			save_patterns(patterns_list, 'pattern/Class/patterns.pkl')

		if option_selected == 6:
		#it deletes the selected pattern from the pattern list
		#but remember to choose 'SAVE' after deleting a pattern, to update the pattern library
			
			patterns_list = delete_pattern(patterns_list)
		
		if option_selected == 7:
		#Finally, to the exit the code
			
			break



data = pd.read_csv('./data/SPY1.csv')
#data that'll be using 

start_technical_analysis(data, R=1.05, bump_factor=1.0, OHLCV='Close')


#### Guessing 2000-02-04