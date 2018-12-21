import ast
from functools import reduce
import numpy as np

class Pattern(object):

	def __init__(self, name, total_extrema_req=5, trading_days=38, tolerance=0.0, signal_value=1.0, no_of_condition=3, no_of_logic=3):
		self.name = name
		self.total_extrema_req = total_extrema_req
		self.trading_days = trading_days
		self.tolerance = tolerance
		self.signal_value = signal_value							#bearish or bullish
		self.no_of_condition = no_of_condition						
		self.no_of_logic = no_of_logic								
		self.condition = []										#conditions like : a[0] > a[1]
		self.logic = []											#logics like : a[0] > a[1] and a[1] > a[2]


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
		condition = list(self.condition)									#condition = self.condition //results in referencing the list 
		tolerance = self.tolerance
		j=0
		while j < self.no_of_condition:
			condition[j] = eval(condition[j])
			j += 1
		i=0
		while i < self.no_of_logic:
			if type(eval(self.logic[i])[0]) is np.bool_:
				compare = bool(eval(self.logic[i])[0])
			else:
				compare = bool(reduce(lambda x, y: x*y, eval(self.logic[i])[0]))
			if compare:
				return bool(eval(self.logic[i])[1])
			else:
				i += 1
				continue
		return False

	def get_name(self):
		return self.name

	def get_trading_days(self):
		return self.trading_days

	def get_total_extrema_req(self):
		return self.total_extrema_req


	def display_pattern(self):
		print '\nName : '+self.name+'\n'
		print '\nTotal Extrema Req : '+str(self.total_extrema_req)+'\n'
		print '\nTrading Days : '+str(self.trading_days)+'\n'
		print '\nTolerance : '+str(self.tolerance)+'\n'
		print '\nSignal Value : '+str(self.signal_value)+'\n'
		i=0
		print '\nConditions : \n'
		while i < len(self.condition):
			print self.condition[i]
			i += 1
		j=0
		print '\nLogics : \n'
		while j < len(self.logic):
			print self.logic[j]
			j += 1



