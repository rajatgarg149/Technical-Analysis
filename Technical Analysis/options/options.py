# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#																		  		  #
#     The file defines technical_analysis() and guessing() methods			      #
# 	  This file imports methods from pattern_library.py, data_validity.py, 	      #
#     pattern.py                                                                  #
# 															                      #
#																	              #
#/////////////////////////////////////////////////////////////////////////////////#




from pattern.pattern_library import select_pattern																	#importing selecting pattern method
from formatcheck.date_validity import date_check																		#importing methods to validate dates
from pattern.patterns import guess_pattern, patterns 																#importing pattern search methods
from datetime import datetime 																				#importing datetime method
from pattern.Class.Pattern import Pattern

def technical_analysis(data, R, patterns_list, OHLCV):
	#data = pricing data
	#R  =   Compression Rate
	#patterns_list = list of patterns available
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}

	pattern_selected = select_pattern(patterns_list)
	patterns(data=data, R=R, pattern=patterns_list[pattern_selected], OHLCV=OHLCV)

def guessing(data, patterns_list, bump_factor, OHLCV, R):
	#data = pricing data
	#patterns_list = list of patterns available
	#bump_factor = factor where, factor*standard_deviation will be added/subtracted to/from current date price
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}
	#R  =   Compression Rate

	valid_trading_days = False					#indicator to check there exists required no. of extrema before the current data within stored no. of trading days
	valid_date = False							#indicator to check whether the mentioned date is a valid trading day

	pattern_selected = select_pattern(patterns_list)
	pattern = patterns_list[pattern_selected]

	while not valid_trading_days:
	#while we do not get a valid pattern
		while not valid_date:
		#while user do not mention a valid trading day
			date = raw_input('\n\tDate : eg. "yyyy-mm-dd" \n')
			end_date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
			valid_date = date_check(data=data, date=end_date)
		valid_trading_days = guess_pattern(pattern=pattern, data=data, date=end_date, bump_factor=bump_factor, OHLCV=OHLCV, R=R)
		valid_date = False
