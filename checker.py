from limited_type import Limited_var


#testvar=Limited_var(limits[0],limits[1],0)

		
def do_test(input):
	limits=[input.min_,input.max_] # test limits
	inputs = ["String test",1100,-200,3.1415,-3.1415] # test inputs
	outputs= [0,limits[1],limits[0],inputs[3],inputs[4]] #required outputs
	fail=0
	print "********Basic testing started!*********"
	for i in range(0,len(inputs)) : 
		print "setting test instance to value %r" % inputs[i]
		input.set(inputs[i])
		out=input.get()
		print "output is : %r" % out
		print "expected is : %r" % outputs[i]
		if (out==outputs[i]):
			print "pass!\n"
		else:
			print "fail!\n"
			fail=1
			
	if (fail==1):
		print "result of test : FAIL"
	else:
		print "Test sucessfully passed!"