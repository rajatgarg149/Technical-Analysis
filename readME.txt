=> IMPORTANT_POINTS.py


-> IMPORTANT_POINTS :

i/p : Time Series(a), Compression Rate(R)			//a is series of price e.g., data.Close
o/p : minmax_list						//minmax_list = (a[iMax or iMin], iMax or iMin, 'Max' or 'Min')

-> FIND_FIRST_TWO :

i/p : Time Series(a), Compression Rate(R)
o/p : (a[iMax], iMax, 'Max'), (a[iMin], iMin, 'Min'), i		//i = current index
								//iMin = index of Minima, a[iMin] = price value of Minima
								//iMax = index of Maxima, a[iMax] = price value of Maxima

-> FIND_MINIMUM :

i/p : Time Series(a), Compression Rate(R), index(i)
o/p : (a[iMin], iMin, 'Min'), i					//i = current index
								//iMin = index of Minima, a[iMin] = price value of Minima

-> FIND_MAXIMUM :

i/p : Time Series(a), Compression Rate(R), index(i)
o/p : (a[iMax], iMax, 'Max'), i					//i = current index 
								//iMax = index of Maxima, a[iMax] = price value of Maxima

------------------------------------------------------------------------------------------------------------------------------------------------------

=> patterns.py

-> patterns :

imports IMPORTANT_POINTS
import Pattern							//Class defined in Pattern.py file

i/p : Time Series(a), Compression Rate(R), pattern(pattern)	//pattern is an object of Pattern class
o/p : pattern_list						//pattern_list = list of (indices of 5(or total_extrema_req) extrema creating pattern)

-> Plotting :

i/p : DataFrame(a), Compression Rate(R), pattern(pattern),	//function gives the plot for the mentioned pattern appearing in given time series
      series_type(OHLCV)					

NOTE:

-> reset_index is used bcoz spliced dataframe has earlier index which needs to be reset to starting index 0
-> To get the ith plot for same pattern_type, change pattern_index[0][] to pattern_index[i][]

------------------------------------------------------------------------------------------------------------------------------------------------------

=> Pattern.py

Class Pattern

Attributes:

-> name
-> total_extrema_req							//total extrema req to define a pattern
-> trading_days								//l+d
-> tolerance								// 0.0, if not any
-> signal_value								//bullish or bearish
-> no_of_condition
-> no_of_logic
-> condition								//conditions like: data[0] > data[2]
-> logic								//logics like : ([condition[0],condition[1],condition[3]], 0)
									//this implies if condition[0] and condition[1] and condition[3] are true
									//then return false

Functions:

-> create_conditions
-> create_logics
-> pattern_recog
-> get_name
-> get_trading_days
-> get_total_extrema_req
-> display_pattern							//outputs all the information of that pattern

------------------------------------------------------------------------------------------------------------------------------------------------------

=> technical_analysis.py

-> used cPickle to store patterns in file. load and save
-> used eval() which takes the raw_input() and itself assigns a data type to the input		//Also used in pattern_recog {Pattern.py}
   e.g., eval(raw_input(2)) --> 2 (int)
	 eval(raw_input(condition[i])) --> condition[i] //outputs the value of condition[i] //if not defined gives error
         eval(raw_input(HS))	       --> //gives error because HS is not defined
 	 eval(raw_input('HS'))	       --> 'HS' (string)

-> also covered ast(abstract syntax tree) 			//only theory //not applied
					  			//but eval() and ast() works in a similar way {read more}

-> it finally outputs a plot showing the existence of that pattern in the data passed	//outputs nothing if there is no existence of such pattern



