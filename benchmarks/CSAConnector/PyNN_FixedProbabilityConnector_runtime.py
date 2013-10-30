from time import time
from sys import argv, exit
from pyNN.nest import setup, Population, IF_cond_alpha, Projection, nest
from pyNN.connectors import FixedProbabilityConnector

if len(argv) != 2:
    print "usage: PyNN_FixedProbabilityConnector_runtime.py <num_neurons>"
    exit()

n = int(argv[1])
setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = Population(n, IF_cond_alpha, {})

# measure random connectivity
start = time()
connector = FixedProbabilityConnector(0.1)
proj = Projection(pop, pop, connector)

nest.sr("memory_thisjob")
mem = nest.spp()
nc = nest.GetKernelStatus("num_connections")
t = time() - start
print "PyNN FixedProbabilityConnector nocsa %i %i %f 0.0 %f %i" % (n, nc, t, t, mem)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "PyNN_FixedProbabilityConnector_runtime.pdf")
