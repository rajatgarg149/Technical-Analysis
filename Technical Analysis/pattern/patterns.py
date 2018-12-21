# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#																		  		  #
#     The file defines the methods that are bottleneck to guessing and technical  #
# 	  and technical analysis. Methods inlcude guess_pattern(), patterns(),   	  #
#     Plotting() and find_minmax_with_index().									  #
# 	  This file imports methods from IMPORTANT_POINTS.py, date_validity.py, 	  #
#     clean.py and class from Pattern.py 										  #
# 	  guess_pattern() search the pattern being guessed and plots if found.        #
#	  patterns() search the pattern through the pricing data and plots if found.  #
#	  Plotting() plots the slected pattern from the list of patterns found.		  #
#	  find_minmax_with_index() returns the price-list and index-list of minima    #
#	  and maxima.																  #
#	  																			  #
#/////////////////////////////////////////////////////////////////////////////////#


from IMPORTANT_POINTS import IMPORTANT_POINTS 			#importing method
from pattern.Class.Pattern import Pattern 							#importing class
from formatcheck.date_validity import trading_day_check				#importing method to validate trading days
from formatcheck.clean import clear									#import clearing terminal method

import numpy as np 										#Matrix and nd-Array library
import pandas as pd 									#Dataframe library
import matplotlib.pyplot as plt 						#Plotting library
#%matplotlib inline




def guess_pattern(pattern, data, date, bump_factor, OHLCV, R):
	#pattern = selected pattern object
	#data = pricing data
	#date = current/last trading date
	#bump_factor = factor where, factor*standard_deviation will be added/subtracted to/from current date price
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}
	#R  =   Compression Rate


	#---------------------------------------------------------------------------------DEFINING VARIABLES------------------------------------------------------------------------------------
	
	minmax_list = IMPORTANT_POINTS(a=data[OHLCV], R=R)
	pattern_list = []
	En = [x[0] for x in minmax_list]
	index = [x[1] for x in minmax_list]
	end_date = date
	end_index = data[data.Date == end_date].index.get_values()[0]			   						#index of the given date
	end_index_price = data.ix[end_index][OHLCV]
	n = len(index)
	name = pattern.get_name()
	trading_days = pattern.get_trading_days()
	total_extrema_req = pattern.get_total_extrema_req()-1											#Since we're guessing therefore, total extrema req = total extrema req(actual) - 1

	#---------------------------------------------------------------------------------LAST EXTREMUM INDEX------------------------------------------------------------------------------------

	index_iter=0
	for index_iter in range(0,len(index)):
		if index[index_iter] > end_index:
			break
	index_iter-=1
	start_index_position = index_iter-total_extrema_req+1
	start_index = index[start_index_position]

	#---------------------------------------------------------------------------------TRACING PATTERN------------------------------------------------------------------------------------
	
	if not trading_day_check(end_index, start_index, trading_days): return False
	
	std = data[ end_index - 38 : end_index ][OHLCV].std()
	indices = index[ start_index_position : index_iter+1 ] + [end_index]							#range of indices will depend on total_extrema_req
	b = En[ start_index_position : index_iter+1 ] + [end_index_price+bump_factor*std]

	if pattern.pattern_recog(b) : pattern_list.append(indices)

	Plotting(data, R, pattern_list, OHLCV)
	return True






def patterns(data, R, pattern, OHLCV):
	#data = pricing data
	#R  =   Compression Rate
	#pattern = selected pattern object
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}

	#---------------------------------------------------------------------------------DEFINING VARIABLES------------------------------------------------------------------------------------
	minmax_list = IMPORTANT_POINTS(a=data[OHLCV], R=R)
	pattern_list = []
	trading_days = pattern.get_trading_days()
	total_extrema_req = pattern.get_total_extrema_req()
	name = pattern.get_name()
	En = [x[0] for x in minmax_list]
	index = [x[1] for x in minmax_list]
	n = len(index)

	#---------------------------------------------------------------------------------TRACING PATTERN---------------------------------------------------------------------------------------
	for i in range(0,n-total_extrema_req+1):
		indices = index[i:i+total_extrema_req]									#range of indices will depend on total_extrema_req
		b = En[i:i+total_extrema_req]
		if index[i+total_extrema_req-1] - index[i] > trading_days :
			continue
		if pattern.pattern_recog(b) :
			pattern_list.append(indices)

	Plotting(data, R, pattern_list, OHLCV)






def Plotting(data, R, pattern_list, OHLCV):
	#data = pricing data
	#R  =   Compression Rate
	#pattern_list = list of patterns found in the pricing data
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}

	#---------------------------------------------------------------------------------DEFINING VARIABLES------------------------------------------------------------------------------------
	
	pattern_index = pattern_list
	index_length = len(pattern_list)
	margin = 5

	#---------------------------------------------------------------------------------CHECKING PATTERNS------------------------------------------------------------------------------------------
	
	if index_length == 0 : 
		print '\nNO PATTERN FOUND!\n'
		return

	#-----------------------------------------------------------------------------------FORMATTING------------------------------------------------------------------------------------------
	
	clear()
	i = 0
	print '\n\tList of patterns found:\n'
	while i < index_length:
		print '\n\t\t'+str(i)+'. '+str(pattern_list[i])+' ['+str(data.loc[pattern_list[i][0], 'Date'])+' TO '+str(data.loc[pattern_list[i][-1], 'Date'])+']'
		i += 1

	#------------------------------------------------------------------------------------PLOTTING------------------------------------------------------------------------------------------
	
	pattern_selected = eval(raw_input('\n\tSelect pattern(type index only) :\n'))
	pattern_index_list = [x for x in pattern_index[pattern_selected]]

	En_max, index_max, En_min, index_min = find_minmax_with_index(data=data, pattern_index_list=pattern_index_list, OHLCV=OHLCV, margin=margin)

	plt.plot(data.loc[pattern_index_list[0]-margin : pattern_index_list[-1]+margin, :].reset_index()[OHLCV], 'b',
				 index_max, En_max, 'g-^', index_min, En_min, 'r-v')
	plt.show()




def find_minmax_with_index(data, pattern_index_list, OHLCV, margin):
	#data = pricing data
	#R  =   Compression Rate
	#pattern_index_list = indices of extrema of pattern selected
	#OHLCV = the pricing type we'll be using {open, high, low, close, volume}
	#margin = margin for plotting before and after gaps to first and last extrema
	
	#-------------------------------------------------------DEFINING VARIABLES-------------------------------------------------------------------------------------
	
	i=0
	pattern_index_list_adjusted = [x + margin - pattern_index_list[0] for x in pattern_index_list]
	extrema_list = [data.loc[x, OHLCV] for x in pattern_index_list]
	temp1 = extrema_list[::2]
	temp2 = extrema_list[1::2]
	temp1_index = pattern_index_list_adjusted[::2]
	temp2_index = pattern_index_list_adjusted[1::2]

	#-------------------------------------------------------FIRST MIN OR MAX--------------------------------------------------------------------------------------
	
	if data.loc[pattern_index_list[0], OHLCV] > data.loc[pattern_index_list[1], OHLCV]:
		return temp1, temp1_index, temp2, temp2_index
	else:
		return temp2, temp2_index, temp1,temp1_index



