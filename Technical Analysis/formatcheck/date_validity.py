# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#                                                                                 #
#     The file defines the methods that checks for the valid date and whether the #
#     sequence lies within specied trading days window.                           #
#                                                                                 #
#/////////////////////////////////////////////////////////////////////////////////#


def date_check(data, date):
	if not data[data.Date == date].index.get_values():
		print '\nCOMMENT : INVALID TRADING DATE!\n'
		return False
	return True

def trading_day_check(end_index, start_index, trading_days):
	if end_index - start_index > trading_days:														#The days between 1st extrema and last extrema must be < trading days
		print '\nCOMMENT : The pattern length exceeds valid no. of tradings days\n'
		return False
	return True
