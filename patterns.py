import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
#%matplotlib inline


from IMPORTANT_POINTS import IMPORTANT_POINTS

data = pd.read_csv('./SPY1.csv')

tolerance = .015
tolerance1 = .0075


def patterns(a, R = 1.05, trading_days = 38):
    minmax_list = IMPORTANT_POINTS(a, R)
    pattern_list = []
    En = [x[0] for x in minmax_list]
    index = [x[1] for x in minmax_list]
    n = len(index)
    for i in range(0,n-4):
        b = En[i:i+5]
        if index[i+4] - index[i] > trading_days :
            pattern_list.append(['None', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
            continue
        if En[i] > En[i+1]:
            if RTOP(b):
                pattern_list.append(['RTOP', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            if HS(b):
                pattern_list.append(['HS', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            if BTOP(b):
                pattern_list.append(['BTOP', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            if TTOP(b):
                pattern_list.append(['TTOP', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            else:
                pattern_list.append(['None', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
        else:
            if RBOT(b):
                pattern_list.append(['RBOT', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            if IHS(b):
                pattern_list.append(['IHS', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            if BBOT(b):
                pattern_list.append(['BBOT', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            if TBOT(b):
                pattern_list.append(['TBOT', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
                continue
            else:
                pattern_list.append(['None', [index[i], index[i+1], index[i+2], index[i+3], index[i+4]]])
    return pattern_list



def HS(a):
    cond1 = (abs(a[0] - (a[0]+a[4])/2) < tolerance*((a[0]+a[4])/2))
    cond2 = (abs(a[1] - (a[1]+a[3])/2) < tolerance*((a[1]+a[3])/2))
    if a[0] < a[1] :
        return False
    if a[2] > a[0] and a[2] > a[4] and cond1 and cond2:
        return True
    return False


def IHS(a):
    cond1 = (abs(a[0] - (a[0]+a[4])/2) < tolerance*((a[0]+a[4])/2))
    cond2 = (abs(a[1] - (a[1]+a[3])/2) < tolerance*((a[1]+a[3])/2))
    if a[0] > a[1] :
        return False
    if a[2] < a[0] and a[2] < a[4] and cond1 and cond2:
        return True
    return False


def BTOP(a):
    if a[0] < a[1]:
        return False
    if a[0] < a[2] and a[2] < a[4] and a[1] > a[3]:
        return True
    return False


def BBOT(a):
    if a[1] < a[0]:
        return False
    if a[0] > a[2] and a[2] > a[4] and a[1] < a[3]:
        return True
    return False


def TTOP(a):
    if a[0] < a[1]:
        return False
    if a[0] > a[2] and a[2] > a[4] and a[1] < a[3]:
        return True
    return False


def TBOT(a):
    if a[0] > a[1]:
        return False
    if a[0] < a[2] and a[2] < a[4] and a[1] > a[3]:
        return True
    return False


def RTOP(a):
    cond1 = (abs(a[0] - (a[0]+a[2]+a[4])/3) < tolerance1*((a[0]+a[2]+a[4])/3))
    cond2 = (abs(a[2] - (a[0]+a[2]+a[4])/3) < tolerance1*((a[0]+a[2]+a[4])/3))
    cond3 = (abs(a[4] - (a[0]+a[2]+a[4])/3) < tolerance1*((a[0]+a[2]+a[4])/3))
    cond4 = (abs(a[1] - (a[1]+a[3])/2) < tolerance1*((a[1]+a[3])/2))
    cond5 = (abs(a[3] - (a[1]+a[3])/2) < tolerance1*((a[1]+a[3])/2))
    cond6 = min(a[0],a[2],a[4]) > max(a[1],a[3])
    if a[0] < a[1]:
        return False
    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
        return True
    return False   


def RBOT(a):
    cond1 = (abs(a[0] - (a[0]+a[2]+a[4])/3) < tolerance1*((a[0]+a[2]+a[4])/3))
    cond2 = (abs(a[2] - (a[0]+a[2]+a[4])/3) < tolerance1*((a[0]+a[2]+a[4])/3))
    cond3 = (abs(a[4] - (a[0]+a[2]+a[4])/3) < tolerance1*((a[0]+a[2]+a[4])/3))
    cond4 = (abs(a[1] - (a[1]+a[3])/2) < tolerance1*((a[1]+a[3])/2))
    cond5 = (abs(a[3] - (a[1]+a[3])/2) < tolerance1*((a[1]+a[3])/2))
    cond6 = min(a[1],a[3]) > max(a[0],a[2],a[4])
    if a[0] > a[1]:
        return False
    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
        return True
    return False    


def DTOP(a):
    if a[0] < a[1]:
        return False


def DBOT(a):
    if a[1] < a[0]:
        return False


def Plotting(a=data, R=1.05, trading_days=38, pattern_type='HS', OHLCV='Close'):
    
    pattern_list = patterns(a=a[OHLCV], R=R, trading_days=trading_days)
    
    #print pattern_list
    
    pattern_HS = [x[1] for x in pattern_list if x[0]=='HS']
    pattern_IHS = [x[1] for x in pattern_list if x[0]=='IHS']
    pattern_TTOP = [x[1] for x in pattern_list if x[0]=='TTOP']
    pattern_TBOT = [x[1] for x in pattern_list if x[0]=='TBOT']
    pattern_RTOP = [x[1] for x in pattern_list if x[0]=='RTOP']
    pattern_RBOT = [x[1] for x in pattern_list if x[0]=='RBOT']
    pattern_BTOP = [x[1] for x in pattern_list if x[0]=='BTOP']
    pattern_BBOT = [x[1] for x in pattern_list if x[0]=='BBOT']
    pattern_DTOP = [x[1] for x in pattern_list if x[0]=='DTOP']
    pattern_DBOT = [x[1] for x in pattern_list if x[0]=='DBOT']
    
    if pattern_type == 'HS': pattern_index = pattern_HS
    if pattern_type == 'IHS': pattern_index = pattern_IHS
    if pattern_type == 'TTOP': pattern_index = pattern_TTOP
    if pattern_type == 'TBOT': pattern_index = pattern_TBOT
    if pattern_type == 'RTOP': pattern_index = pattern_RTOP
    if pattern_type == 'RBOT': pattern_index = pattern_RBOT
    if pattern_type == 'BTOP': pattern_index = pattern_BTOP
    if pattern_type == 'BBOT': pattern_index = pattern_BBOT
    if pattern_type == 'DTOP': pattern_index = pattern_DTOP
    if pattern_type == 'DBOT': pattern_index = pattern_DBOT
    
    if len(pattern_index) == 0 : return
    
    #print pattern_index
    
    
    #minmax_list = IMPORTANT_POINTS(a=a.loc[pattern_index[0][0]:pattern_index[0][4], :].reset_index()[OHLCV], R=R)
    
    #En_max = [x[0] for x in minmax_list if x[2]=='Max']
    #index_max = [x[1] for x in minmax_list if x[2]=='Max']
    
    #En_min = [x[0] for x in minmax_list if x[2]=='Min']
    #index_min = [x[1] for x in minmax_list if x[2]=='Min']
    
    if pattern_type == ('HS' or 'TTOP' or 'RTOP' or 'BTOP' or 'DTOP'):
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


#Plotting(a=data, R=1.05, trading_days=38, pattern_type='TBOT', OHLCV='Close')


