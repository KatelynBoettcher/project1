import numpy
import matplotlib.pyplot as plt
a = numpy.loadtxt('samples/0.raw', skiprows=1, delimiter=',')
plt.plot(a[:,0], a[:,1])
plt.show()
print(len(a))
