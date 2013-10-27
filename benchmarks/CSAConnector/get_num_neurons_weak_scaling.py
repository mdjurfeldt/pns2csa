# from numpy import array, ones, sqrt
# num_conn_optimal = [48000**2*0.1/(48/x) for x in (1,2,4,6,12,24,48)]
# num_neurons = [sqrt(x*10) for x in num_conn_optimal]
# num_conn_real = [round(x)**2*0.1 for x in num_neurons]
# error = ones(7) - array(num_conn_real) / array(num_conn_optimal) * 1000
# print "num_neurons for 1,2,4,6,12,24,48 processes:", array(num_neurons).round()
# print "error in permil: min=%f, max=%f" % (min(error), max(error))

from math import sqrt
from sys import argv
print int(sqrt(48000**2 * int(argv[1]) / 48))
