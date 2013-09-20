from time import time
from sys import argv, exit
from pyNN.nest import setup, Population, IF_cond_alpha, CSAConnector, Projection
import csa

if len(argv) != 2:
    print "usage: PyNN_native.py <num_neurons>"
    sys.exit()

setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = Population(int(argv[1], IF_cond_alpha, {})

# measure full connectivity
start = time()
cset = csa.full
connector = CSAConnector(cset)
proj = Projection(pop, pop, connector)
print "Time for native CSA interface (full):", time() - start

# measure random connectivity



#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "PyNN_native.pdf")
