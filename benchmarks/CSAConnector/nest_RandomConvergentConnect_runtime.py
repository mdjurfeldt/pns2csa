from time import time
from sys import argv, exit
from pyNN.nest import setup, nest

if len(argv) != 2:
    print "usage: nest_RandomConvergentConnect_runtime.py <num_neurons>"
    exit()

n = int(argv[1])
setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = nest.Create("iaf_neuron", n)

# measure random connectivity
start = time()
nest.RandomConvergentConnect(pop, pop, int(n*n*0.1))

nest.sr("memory_thisjob")
mem = nest.spp()
nc = nest.GetKernelStatus("num_connections")
t = time() - start
print "nest RandomConvergentConnect nocsa %i %i %f 0.0 %f %i" % (n, nc, t, t, mem)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "nest_RandomConvergentConnect_runtime.pdf")
