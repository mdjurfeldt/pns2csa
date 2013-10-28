from time import time
from sys import argv, exit
from pyNN.nest import setup, Population, IF_cond_alpha, CSAConnector, Projection, nest
import csa

if len(argv) != 2:
    print "usage: nest_CSAConnector_csa_runtime.py <num_neurons>"
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
nest.sli_run("preptime"); preptime = nest.sli_pop()
nest.sli_run("itertime"); itertime = nest.sli_pop()
print "nest CSAConnector random(0.1) csa %i %i %f %f %f %i" % (n, nc, time() - start, preptime, itertime, mem)

# measure one-to-one connectivity
start = time()
cset = csa.oneToOne
connector = CSAConnector(cset)
proj = Projection(pop, pop, connector)

nc = nest.GetKernelStatus("num_connections") - nc
nest.sli_run("preptime"); preptime = nest.sli_pop()
nest.sli_run("itertime"); itertime = nest.sli_pop()
print "nest CSAConnector oneToOne csa %i %i %f %f %f 0" % (n, nc, time() - start, preptime, itertime)

#import nest.visualization as vis
#vis.plot_network(pop.all_cells, "nest_CSAConnector_csa_runtime.pdf")
