from limited_type import Limited_var


#testvar=Limited_var(limits[0],limits[1],0)

		
def do_test(input):
	limits=[input.min_,input.max_] # test limits
	test_info=["testing string","out of range test : upper","out of range test : lower","testing floating point","in-range test ","down limit test","up limit test","near out of range","near out of range negative"]
	inputs = ["String test",input.max_+10,input.min_-10,float(((float(input.max_)+float(input.min_))/2.0)-(float(input.max_)-float(input.min_))/10.0),((input.max_+input.min_)//2),input.min_,input.max_,input.min_-0.0006,input.max_+0.0006] # test inputs
	outputs= [0,limits[1],limits[0],inputs[3],inputs[4],limits[0],limits[1],limits[0],limits[1]] #required outputs
	
	fail=0
	print "********Basic testing started!*********"
	for i in range(0,len(inputs)) : 
		print "%d : %s"%(i+1,test_info[i])
		print "setting test instance to value %r" % inputs[i]
		input.set(inputs[i])
		out=input.get()
		print "output is : %r" % out
		print "expected is : %r" % outputs[i]
		if (type(outputs[i]) is str):
			print "converting input to string for comparation" 
			out="%r"%input.get()
			if (out==(outputs[i])):
				print "string pass!\n"
			else :
				fail=1
				print "string fail!\n"
		else:
			if (out==outputs[i]):
				print "pass!\n"
			else:
				print "fail!\n"
				fail=1
				
	if (fail==1):
		print "result of test : FAIL"
	else:
		print "Test sucessfully passed!"
	
	print "------Instance info------"
	print "minimum limitation : %r"%input.min_
	print "maximum limitation : %r"%input.max_
	print "value : %r"%input.get()