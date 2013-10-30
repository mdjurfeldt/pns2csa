from time import time
from sys import argv, exit
from pyNN.nest import setup, nest

if len(argv) != 3:
    print "usage: nest_RandomConvergentConnect_scaling.py <num_neurons> <num_procs>"
    exit()

n = int(argv[1])
np = int(argv[2])
setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = nest.Create("iaf_neuron", n)

# measure random connectivity
start = time()
nest.RandomConvergentConnect(pop, pop[:1], int(n*n*0.1))

rank = nest.Rank()
nc = nest.GetKernelStatus("num_connections")
t = time() - start
print "nest RandomConvergentConnect nocsa %i %i %f 0.0 %f %i %i" % (n, nc, t, t, rank, np)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "nest_RandomConvergentConnect_scaling.pdf")
