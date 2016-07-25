from limited_type import Limited_var


#testvar=Limited_var(limits[0],limits[1],0)

		
def do_test(input):
	limits=[input.min_,input.max_] # test limits
	test_info=["testing string","out of range test : upper","out of range test : lower","testing floating point","in-range test ","down limit test","up limit test","near out of range","near out of range negative"]
	inputs = ["String test",input.max_+10,input.min_-10,float(((float(input.max_)+float(input.min_))/2.0)-(float(input.max_)-float(input.min_))/10.0),((input.max_+input.min_)//2),input.min_,input.max_,input.min_-0.0006,input.max_+0.0006] # test inputs
	outputs= [0,limits[1],limits[0],inputs[3],inputs[4],limits[0],limits[1],limits[0],limits[1]] #required outputs
	
	
	print "********Basic testing started!*********"
	for i in range(0,len(inputs)) : 
		print "%d : %s"%(i+1,test_info[i])
		print "setting test instance to value %r" % inputs[i]
		input.set(inputs[i])
		out=input.get()
		assert (out==outputs[i]),"result error : excepted value is %r but got %r"%(outputs[i],out)
	print "sucess"	