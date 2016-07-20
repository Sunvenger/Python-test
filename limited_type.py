
class Limited_var:
	max_=0 # Maximum assignable value
	min_=0 # Minimum assignable value
	__value=0
	def __init__(self,min, max,val):
		self.max_=max
		self.min_=min
		__value=val
	
	def display_(self):
		return self.value
	
	def set(self,val):
		if (type(val) is str):
			self.__value=0
		else:	
			self.__value=float(max(min(self.max_,val),self.min_));
		
	def set_lim(self,*val): # setter limits
		
		min,max=val
		
	def get(self):
		return self.__value
		
	def __str__(self):
		return "%r"%self.__value
		
	def __int__(self):
		return self.__value
		
	def __add__(self, other):
		return self.__value + other
		
	def __radd__(self, other):
		return self.__value + other


