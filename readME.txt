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
tolerance = .015						//tolerance set for HS and IHS
tolerance1 = .0075						//tolerance1 set for RTOP and RBOT

i/p : Time Series(a), Compression Rate(R), l+d(trading_days)	//l+d = l is window length, d is a stretch to let the pattern complete
o/p : pattern_list						//pattern_list = list of (pattern_type, [indices of 5 extrema creating pattern])

-> HS(a), IHS(a), BTOP(a), BBOT(a), TTOP(a), TBOT(a),		//functions taking set of 5 extrema within l+d days of interval as an i/p 
   RTOP(a), RBOT(a), DTOP(a), DBOT(a)				//and o/p whether the particular pattern is possible

-> ltop_gt_hbot(a)						//i/p is a set of 5 extrema withing l+d trading days
								//o/p is whether lowest top > highest bottom

-> Plotting :

i/p : DataFrame(a), Compression Rate(R), l+d(trading_days),	//function gives the plot for the mentioned pattern appearing in given time series type
      pattern_type(pattern_type), series_type(OHLCV)		//within l+d trading days compressed using R

NOTE:

-> reset_index is used bcoz spliced dataframe has earlier index which needs to be reset to starting index 0
-> To get the ith plot for same pattern_type, change pattern_index[0][] to pattern_index[i][]
-> pattern_TYPE is list of pattern indices consitituting pattern of that TYPE







