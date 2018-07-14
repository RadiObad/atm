the_amount = 500
request = 277
resulat = the_amount - request
while request > 0:
	if request > 100:
		print "give" + str(100)
		request = request - 100
	elif request > 50:
		print"give" + str(50)
		request = request -50
	elif request > 10:
		print"give" + str(10)
		request = request -10
	elif request > 5:
		print"give" + str(5)
		request = request -5
		
	else:
		print "give" + str(request)
		request = request -request	
	#request = 0		
print request	
			
	
