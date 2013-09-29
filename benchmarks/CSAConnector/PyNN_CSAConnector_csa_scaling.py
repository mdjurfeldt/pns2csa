from time import time
from sys import argv, exit
from pyNN.nest import setup, Population, IF_cond_alpha, Projection, nest
from pyNN.connectors import CSAConnector
import csa

if len(argv) != 2:
    print "usage: PyNN_CSAConnector_csa_scaling.py <num_neurons>"
    exit()

n = int(argv[1])
setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = Population(n, IF_cond_alpha, {})

# measure random connectivity
start = time()
cset = csa.random(0.1)
connector = CSAConnector(cset)
proj = Projection(pop, pop, connector)
rank = nest.Rank()
print "PyNN CSAConnector random(0.1) csa %i %f %i" % (n, time() - start, rank)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "PyNN_CSAConnector_csa_scaling.pdf")
