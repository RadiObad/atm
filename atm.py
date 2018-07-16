# allowed papers: 100, 50, 10, 5, and cents


class ATM():
	amount = 200
	def __init__(self, balance, bank_name):
		self.balance = balance	
		self.bank_name	= bank_name	

	def withdraw(self, request):	
		self.balance = self.balance - request
		if request > self.balance:
			print "Can't give you all this menoy !!"
		elif request < 0:
			print "More than zero plz!"
		else:		 
			while request > 0:

				if request >= 100:
					print "give 100"
					request -= 100
				
				elif request >= 50:
					print"give 50"
					request -= 50
				
				elif request >= 10:
					print"give 10"
					request -= 10
				
				elif request >= 5:
					print"give 5"
					request -= 5
				
				else:
					print "give " + str(request)
					request -= request	
			#request = 0		
		return self.balance	


atm1 = ATM(0,"Smart Bank")			
print atm1.withdraw(223)			
print atm1.withdraw(900)	


#atm2 = ATM(500, "Any ?Bank")
#atm2.withdraw(233)