from time import time
from sys import argv, exit
from pyNN.nest import setup, Population, IF_cond_alpha, Projection, nest
from pyNN.connectors import CSAConnector
import libcsa as csa

if len(argv) != 3:
    print "usage: PyNN_CSAConnector_libcsa_scaling.py <num_neurons> <num_procs>"
    exit()

n = int(argv[1])
np = int(argv[2])
setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = Population(n, IF_cond_alpha, {})

# measure random connectivity
start = time()
cset = csa.random(0.1)
connector = CSAConnector(cset)
proj = Projection(pop, pop, connector)
rank = nest.Rank()
print "PyNN CSAConnector random(0.1) libcsa %i %f %i" % (n, time() - start, rank, np)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "PyNN_CSAConnector_libcsa_scaling.pdf")
