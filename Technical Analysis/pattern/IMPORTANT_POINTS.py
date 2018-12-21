# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#                                                                                 #
#     The file defines the methods that results in finding extrema through time   #
#     series of pricing data.                                                     #
#                                                                                 #
#/////////////////////////////////////////////////////////////////////////////////#



def IMPORTANT_POINTS(a, R):
    #a = time series of pricing data    //NOTE: time series is a series of choosen price-type from whole data e.g., data['Close'] is a series of closing prices. 
    #R= Compression Rate

    minmax_list = []
    temp_1, temp_2, i = FIND_FIRST_TWO(a, R)

    minmax_list.append(temp_1)
    minmax_list.append(temp_2)
    n = len(a)
    if i < n and a[i-1] > a[0]:
        temp, i = FIND_MINIMUM(a, R, i)
        minmax_list.append(temp)
    while i < n:
        temp1, i = FIND_MAXIMUM(a, R, i)
        minmax_list.append(temp1)                              # 
        if i < n:                                              #    CHANGED   [ADDED 'if' CONDITION]
            temp2, i = FIND_MINIMUM(a, R, i)                   #
            minmax_list.append(temp2)
    return minmax_list


def FIND_FIRST_TWO(a, R):
    #a = time series of pricing data    //NOTE: time series is a series of choosen price-type from whole data e.g., data['Close'] is a series of closing prices. 
    #R= Compression Rate

    #-------------------------------------------------------DEFINING VARIABLES------------------------------------------------------------------------------------
    i = 0
    iMin = 1
    iMax=1
    n = len(a)

    #-------------------------------------------------------Conditions for maxima and minima------------------------------------------------------------------------------------
    while i < n and a[i]/a[iMin] < R and a[iMax]/a[i] < R:
    #while no minima or maxima found

        if a[i] < a[iMin]:
            iMin = i
        if a[i] > a[iMax]:
            iMax = i
        i = i+1

    #-------------------------------------------------------First extrema is Min or Max-----------------------------------------------------------------------------
    if iMin < iMax:
        return (a[iMin], iMin, 'Min'), (a[iMax], iMax, 'Max'), i
    else:
        return (a[iMax], iMax, 'Max'), (a[iMin], iMin, 'Min'), i


def FIND_MINIMUM(a, R, i):
    #a = time series of pricing data    //NOTE: time series is a series of choosen price-type from whole data e.g., data['Close'] is a series of closing prices. 
    #R= Compression Rate
    #i = index in time series to start searching with

    #-------------------------------------------------------DEFINING VARIABLES------------------------------------------------------------------------------------
    iMin = i
    n = len(a)

    #-------------------------------------------------------Conditions for minima------------------------------------------------------------------------------------
    while i < n and a[i]/a[iMin] < R:
    #while no minima found

        if a[i] < a[iMin]:
            iMin = i
        i = i+1

    return (a[iMin], iMin, 'Min'), i

def FIND_MAXIMUM(a, R, i):
    #a = time series of pricing data    //NOTE: time series is a series of choosen price-type from whole data e.g., data['Close'] is a series of closing prices. 
    #R= Compression Rate
    #i = index in time series to start searching with

    #-------------------------------------------------------DEFINING VARIABLES------------------------------------------------------------------------------------
    iMax = i
    n = len(a)

    #-------------------------------------------------------Conditions for maxima-----------------------------------------------------------------------------------
    while i < n and a[iMax]/a[i] < R:
    #while no maxima found

        if a[i] > a[iMax]:
            iMax = i
        i = i+1

    return (a[iMax], iMax, 'Max'), i


