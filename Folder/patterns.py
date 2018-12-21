import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
#%matplotlib inline


from IMPORTANT_POINTS import IMPORTANT_POINTS
from Pattern import Pattern

data = pd.read_csv('./SPY1.csv')

tolerance = .015
tolerance1 = .0075


def patterns(a, R, pattern):
    minmax_list = IMPORTANT_POINTS(a, R)
    pattern_list = []
    En = [x[0] for x in minmax_list]
    index = [x[1] for x in minmax_list]
    n = len(index)
    trading_days = pattern.get_trading_days()
    total_extrema_req = pattern.get_total_extrema_req()
    name = pattern.get_name()
    for i in range(0,n-total_extrema_req+1):
    	indices = index[i:i+total_extrema_req]
        b = En[i:i+total_extrema_req]
        if index[i+total_extrema_req-1] - index[i] > trading_days :
            continue
        if pattern.pattern_recog(b) :
        	pattern_list.append(indices)
    return pattern_list




def Plotting(a, R, pattern, OHLCV):
    
    pattern_list = patterns(a=a[OHLCV], R=R, pattern=pattern)

    pattern_index = pattern_list

    if len(pattern_index) == 0 : return

    if a.loc[pattern_index[0][0], 'Close'] > a.loc[pattern_index[0][1], 'Close']:
        #print pattern_type
        En_max = [a.loc[pattern_index[0][0], 'Close'], a.loc[pattern_index[0][2], 'Close'], a.loc[pattern_index[0][4], 'Close']]
        index_max = [pattern_index[0][0]+5 - pattern_index[0][0], pattern_index[0][2]+5 - pattern_index[0][0], pattern_index[0][4]+5 - pattern_index[0][0]]
        
        En_min = [a.loc[pattern_index[0][1], 'Close'], a.loc[pattern_index[0][3], 'Close']]
        index_min = [pattern_index[0][1]+5 - pattern_index[0][0], pattern_index[0][3]+5 - pattern_index[0][0]]
        
        #print En_min, En_max, index_min, index_max
        
    else:
        En_min = [a.loc[pattern_index[0][0], 'Close'], a.loc[pattern_index[0][2], 'Close'], a.loc[pattern_index[0][4], 'Close']]
        index_min = [pattern_index[0][0]+5 - pattern_index[0][0], pattern_index[0][2]+5 - pattern_index[0][0], pattern_index[0][4]+5 - pattern_index[0][0]]
        
        En_max = [a.loc[pattern_index[0][1], 'Close'], a.loc[pattern_index[0][3], 'Close']]
        index_max = [pattern_index[0][1]+5 - pattern_index[0][0], pattern_index[0][3]+5 - pattern_index[0][0]]
        
        #print En_min, En_max, index_min, index_max
    
    plt.plot(a.loc[pattern_index[0][0]-5:pattern_index[0][4]+5, :].reset_index()[OHLCV], 'b', index_max, En_max, 'g^', index_min, En_min, 'rv')
    plt.show()


