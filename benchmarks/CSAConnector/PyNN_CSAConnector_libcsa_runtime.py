from time import time
from sys import argv, exit
from pyNN.nest import setup, Population, IF_cond_alpha, Projection, nest
from pyNN.connectors import CSAConnector
import libcsa as csa

if len(argv) != 2:
    print "usage: PyNN_CSAConnector_libcsa_runtime.py <num_neurons>"
    exit()

n = int(argv[1])
setup(timestep=0.1, min_delay=0.1, max_delay=4.0)
pop = Population(n, IF_cond_alpha, {})

# measure random connectivity
start = time()
cset = csa.random(0.1)
connector = CSAConnector(cset)
proj = Projection(pop, pop, connector)

nest.sr("memory_thisjob")
mem = nest.spp()
nc = nest.GetKernelStatus("num_connections")
t = time() - start
print "PyNN CSAConnector random(0.1) libcsa %i %i %f 0.0 %f %i" % (n, nc, t, t, mem)

# measure one-to-one connectivity
start = time()
cset = csa.oneToOne
connector = CSAConnector(cset)
proj = Projection(pop, pop, connector)

nc = nest.GetKernelStatus("num_connections") - nc
t = time() - start
print "PyNN CSAConnector oneToOne libcsa %i %i %f 0.0 %f 0" % (n, nc, t, t)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "PyNN_CSAConnector_libcsa_runtime.pdf")
