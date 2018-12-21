# ////////////////////////////////  DESCRIPTION  /////////////////////////////////#
#																		  		  #
#     The file defines the Pattern class and its elements. 				 	      #
# 	  Methods like get_name(), get_tradings_days() and get_total_extrema_req() to #
# 	  get the details. create_conditions() and create_logics() to add conditions  #
#	  and logics. pattern_recog() to validate patterns given extrema, conditions  #
#	  and logics. display_pattern() to display pattern attribute values			  #
#	  																			  #
#/////////////////////////////////////////////////////////////////////////////////#



from functools import reduce
import numpy as np                                          				#Matrix and nd-Array library

class Pattern(object):

	def __init__(self, name, total_extrema_req=5, trading_days=38, tolerance=0.0, signal_value=1.0, no_of_condition=3, no_of_logic=3):
		self.name = name
		self.total_extrema_req = total_extrema_req
		self.trading_days = trading_days
		self.tolerance = tolerance
		self.signal_value = signal_value									#bearish or bullish
		self.no_of_condition = no_of_condition						
		self.no_of_logic = no_of_logic								
		self.condition = []													#conditions like : a[0] > a[1]
		self.logic = []														#logics like : a[0] > a[1] and a[1] > a[2]

	def get_name(self):
		return self.name

	def get_trading_days(self):
		return self.trading_days

	def get_total_extrema_req(self):
		return self.total_extrema_req


	def create_conditions(self):
		i=0
		while i < self.no_of_condition:
			self.condition.append(raw_input('\nCondition'+str(i)+' :\n'))
			i += 1

	def create_logics(self):
		i=0
		while i < self.no_of_logic:
			self.logic.append(raw_input('\nLogic'+str(i)+' :\n'))
			i += 1

	def pattern_recog(self, data):
		#data = list of extrema
		#we may get confuse where the data is getting used
		#eval, condition and logic take care of it.
		#See the pattern info of sample patterns stored
		
		condition = list(self.condition)									#condition = self.condition //results in referencing the list 
		tolerance = self.tolerance
		j=0
		while j < self.no_of_condition:
			condition[j] = eval(condition[j])
			j += 1
		i=0
		while i < self.no_of_logic:
			if type(eval(self.logic[i])[0]) is np.bool_:					#Output of eval(self.logic[i])[0] is of numpy.bool_ type
				compare = bool(eval(self.logic[i])[0])
			else:
				compare = bool(reduce(lambda x, y: x*y, eval(self.logic[i])[0]))
			if compare:														#if compare i.e, logic is true then it should return the mentioned output
				return bool(eval(self.logic[i])[1])
			else:
				i += 1
				continue
		return False


	def display_pattern(self):
		print '\n\t\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\  PATTERN '+self.name+'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ '
		print '\n\t\tName : '+self.name+'\tTotal Extrema Req : '+str(self.total_extrema_req)+'\tTrading Days : '+str(self.trading_days)+'\n'
		print '\n\t\tTolerance : '+str(self.tolerance)+'\tSignal Value : '+str(self.signal_value)+'\n'
		i=0
		print '\n\tConditions : \n'
		while i < len(self.condition):
			print '\t\t'+self.condition[i]
			i += 1
		j=0
		print '\n\tLogics : \n'
		while j < len(self.logic):
			print '\t\t'+self.logic[j]
			j += 1



