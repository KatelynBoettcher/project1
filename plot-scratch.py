import numpy
import matplotlib.pyplot as plt
a = numpy.loadtxt('samples/0.raw', skiprows=1, delimiter=',')
plt.plot(a[:,0], a[:,1])
plt.show()
print(len(a))

#I want to get the slopes of the initil linear sections (Young's modulus)
	#Find initial linear section (differing numbers of points!)
	#Use stuff from notebook 4(3?) to get linear regression of initial section 

#I want to average slopes over all of the samples

