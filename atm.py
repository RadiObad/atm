# allowed papers: 100, 50, 10, 5, and cents

amount = 500

#request = 567

def withdraw(amount,request):	
	Balance_restante = amount - request
	if request > amount:
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
	return Balance_restante	
			
amount =  withdraw(amount,300)
print amount

amount = withdraw(amount,30)
print amount

amount = withdraw(amount,5)
print amount