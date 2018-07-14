# allowed papers: 100, 50, 10, 5, and cents

amount = 800

#request = 300
request = 721
#request = 555	
lst = [100,50,10,5,2,1]
if request > amount:
	print "Can't give you all this menoy !!"
elif request < 0:
	print "More than zero plz!"
else:
	for p in lst:
		while request >= p:
			print "give " + str(p)
			request -= p



	
