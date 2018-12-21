from Pattern import Pattern
from patterns import patterns, Plotting

import numpy as np
import pandas as pd
import ast
import cPickle as pickle					#faster than Pickle

def start_technical_analysis(data, OHLCV):
	patterns = load_patterns('patterns.pkl')
	while(1):
		answer = eval(raw_input('Choose option: \n1. Technical Analysis \n2. Pattern Info \n3. Add Pattern \n4. Save \n5. Exit\n'))
		if answer == 1:

			i = 0
			print 'List of patterns:'
			while i < len(patterns):
				print '\n'+str(i)+'. '+patterns[i].get_name()
				i += 1
			
			pattern_selected = eval(raw_input('Select pattern(type index only) :\n'))
			Plotting(a=data, R=1.05, pattern=patterns[pattern_selected], OHLCV='Close')


		if answer == 2:
			
			i = 0
			print 'List of patterns:'
			while i < len(patterns):
				print '\n'+str(i)+'. '+patterns[i].get_name()
				i += 1
			
			pattern_selected = eval(raw_input('Select pattern(type index only) :\n'))
			patterns[pattern_selected].display_pattern()

		if answer == 3:
			
			name = eval(raw_input('Specify following info: \nName\n'))
			total_extrema_req = eval(raw_input('\nTotal Extrema Required For Detection\n'))
			trading_days = eval(raw_input('\nTrading Days\n'))
			tolerance = eval(raw_input('\nTolerance(0.0, if not any)\n'))
			signal_value = eval(raw_input('\nSignal Value(Bullish = 1, Bearish = -1)\n'))
			no_of_condition = eval(raw_input('\nNo of Conditions(like : data[0] > data[1])\n'))
			no_of_logic = eval(raw_input('\nNo of Logics(like : (condition[1] and condition[2], False)\n'))
			
			patterns.append(Pattern(name=name, total_extrema_req=total_extrema_req, trading_days=trading_days, tolerance=tolerance, signal_value=signal_value,
				no_of_condition=no_of_condition, no_of_logic=no_of_logic))
			
			patterns[len(patterns)-1].create_conditions()
			patterns[len(patterns)-1].create_logics()

		if answer == 4:
			
			save_patterns(patterns, 'patterns.pkl')

		if answer == 5:
			
			break

def load_patterns(filename):
	patterns = []
	try:
		with open(filename, 'rb') as input:
			patterns = pickle.load(input)
	except IOError:
		return patterns
	return patterns

def save_patterns(patterns,filename):
	with open(filename, 'wb') as output:
		pickle.dump(patterns, output, pickle.HIGHEST_PROTOCOL)					#protocol is the format to store the data stream



data = pd.read_csv('./SPY1.csv')
start_technical_analysis(data, 'Close')