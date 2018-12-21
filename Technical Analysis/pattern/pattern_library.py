# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#																		  		  #
#     The file defines load_patterns(), save_patterns(), create_pattern()	      #
#  	  delete_pattern(), select_pattern() and display_pattern()					  #
# 	  This file imports method from clean.py and class from Pattern.py 			  #
# 															                      #
#																	              #
#/////////////////////////////////////////////////////////////////////////////////#



import cPickle as pickle																	#library to store serialized python objects #faster than Pickle
from formatcheck.clean import clear 																	#import clearing terminal method
from Class.Pattern import Pattern 																#import Pattern class

def load_patterns(filename):
	#filename = path to file patterns are stored in
	patterns_list = []
	try:
		with open(filename, 'rb') as input:
		#read the patterns in pattern list from the file
			patterns_list = pickle.load(input)
	except IOError:
		return patterns_list
	return patterns_list

def save_patterns(patterns_list,filename):
	#patterns_list = list of patterns available
	#filename = path to file we want the patterns to be stored in

	with open(filename, 'wb') as output:
	#write the patterns in pattern list to the file
		pickle.dump(patterns_list, output, pickle.HIGHEST_PROTOCOL)							 #protocol is the format to store the data stream


def create_pattern():
	
	clear()
	name = eval(raw_input("\n\tSpecify following info: \n\t\tName(type it like 'incursio')\n"))
	total_extrema_req = eval(raw_input('\n\t\tTotal Extrema Required For Detection\n'))
	trading_days = eval(raw_input('\n\t\tTrading Days\n'))
	tolerance = eval(raw_input('\n\t\tTolerance(0.0, if not any)\n'))
	signal_value = eval(raw_input('\n\t\tSignal Value(Bullish = 1, Bearish = -1)\n'))
	no_of_condition = eval(raw_input('\n\t\tNo of Conditions(like : data[0] > data[1])\n'))
	no_of_logic = eval(raw_input('\n\t\tNo of Logics(like : (condition[1] and condition[2], False)\n'))
	
	new_pattern =  Pattern(name=name, total_extrema_req=total_extrema_req, trading_days=trading_days, tolerance=tolerance, signal_value=signal_value,
						no_of_condition=no_of_condition, no_of_logic=no_of_logic)
	new_pattern.create_conditions()
	new_pattern.create_logics()
	
	return new_pattern

def delete_pattern(patterns_list):
	#patterns_list = list of patterns available

	pattern_selected = select_pattern(patterns_list)
	del patterns_list[pattern_selected]

	return patterns_list

def select_pattern(patterns_list):
	#patterns_list = list of patterns available

	clear()
	i = 0
	print '\n\tList of patterns:\n'
	while i < len(patterns_list):
		print '\n\t\t'+str(i)+'. '+patterns_list[i].get_name()
		i += 1
	pattern_selected = eval(raw_input('\n\tSelect pattern (type index only) :\n'))
	
	return pattern_selected
	

def display_pattern(patterns_list):
	#patterns_list = list of patterns available

	pattern_selected = select_pattern(patterns_list)
	clear()
	patterns_list[pattern_selected].display_pattern()
