import re
import matplotlib
matplotlib.use('Agg')
import pylab
import numpy
import operator

colors = {"nest": "#ff6633", "PyNN": "#31cd32"}
styles = {"libcsa": "--", "csa": "-"}

pylab.rc("axes", labelsize=14, titlesize=14)
pylab.rc("xtick", labelsize=14)
pylab.rc("ytick", labelsize=14)
pylab.rc("font", size=14)
pylab.rc("legend", fontsize=14)

datafile = "data.log"
with open(datafile) as f:
    rawdata = f.readlines()

data = {}
connectors = set()
for line in rawdata:

    d = line.split()

    pynn_component = d[0]
    connector = d[2]
    connectors.add(connector)
    library = d[3]
    n_neurons = int(d[4])
    time = float(d[5])
    memory = int(d[6])

    try:
        data[connector][(pynn_component, library)].append((n_neurons, time, memory))
    except: # connector not in data, or (mode, library) not in data[connector]
        try:
            data[connector][(pynn_component, library)] = [(n_neurons, time, memory)]    
        except: # connector not in data
            data[connector] = {(pynn_component, library): [(n_neurons, time, memory)]}

for connector in connectors:

    fig1 = pylab.figure(figsize=(6,4))
    ax1 = fig1.add_subplot(1,1,1)
    ax1.yaxis.grid(color='gray', linestyle='dashed')

    fig2 = pylab.figure(figsize=(6,4))
    ax2 = fig2.add_subplot(1,1,1)
    ax2.yaxis.grid(color='gray', linestyle='dashed')

    for (i, ((pynn_component, library), values)) in enumerate(data[connector].items()):

        v = numpy.sort(numpy.array(values),0)
        n, t, m = v[:,0], v[:,1], v[:,2]
        color = colors[pynn_component]
        style = styles[library]

        slope, _ = numpy.polyfit(numpy.log(n), numpy.log(t), 1)
        label = ", ".join((pynn_component, library, "%.2f" % slope))
        ax1.loglog(n, t, lw=2, marker="o", linestyle=style, label=label,
                   color=color, zorder=i+100)

        linear_t = [t[0]*float(x)/n[0] for x in n]
        ax1.loglog(n, linear_t, lw=4, c="#dddddd", zorder=i)
        ax1.loglog(n, linear_t, lw=2, c="#eeeeee", zorder=i)

        slope, _ = numpy.polyfit(numpy.log(n), numpy.log(m), 1)
        label = ", ".join((pynn_component, library, "%.2f" % slope))
        ax2.loglog(n, m/1024.0, lw=2, marker="o", linestyle=style, label=label,
                   color=color, zorder=i+100)
     
        linear_m = [m[0]*float(x)/n[0] for x in n]
        ax2.loglog(n, linear_m, lw=4, c="#dddddd", zorder=i)
        ax2.loglog(n, linear_m, lw=2, c="#eeeeee", zorder=i)
    
    fig1.subplots_adjust(left=0.14, bottom=0.1, right=0.96, top=0.91)
    fig2.subplots_adjust(left=0.14, bottom=0.1, right=0.96, top=0.91)
    
    ax1.set_title("Run time of CSAConnector(%s)" % connector)
    ax2.set_title("Memory usage of CSAConnector(%s)" % connector)

    ax1.set_xlabel("number of neurons")
    ax2.set_xlabel("number of neurons")

    ax1.set_ylabel("wallclock time (s)")
    ax2.set_ylabel("memory consumption (MiB)")

    handles, labels = ax1.get_legend_handles_labels()
    hl = sorted(zip(handles, labels), key=operator.itemgetter(1))
    handles, labels = zip(*hl)
    ax1.legend(handles, labels, title="connector, library, slope",
               fancybox=True, loc="best", numpoints=1)

    handles, labels = ax2.get_legend_handles_labels()
    hl = sorted(zip(handles, labels), key=operator.itemgetter(1))
    handles, labels = zip(*hl)
    ax2.legend(handles, labels, title="connector, library, slope",
               fancybox=True, loc="best", numpoints=1)

    fname = "CSAConnector_%s.svg" % connector
    fig1.savefig(fname)
    print "saved '%s'" % fname

    if "random" in connector:
        fname = "CSAConnector_mem_%s.svg" % connector
        fig2.savefig(fname)
        print "saved '%s'" % fname


import svgutils.transform as sg

fig1 = sg.fromfile("CSAConnector_random(0.1).svg")
plot1 = fig1.getroot()
plot1.moveto(0, 10)
txt1 = sg.TextElement(10, 20, "A", size=18, weight="bold")

fig2 = sg.fromfile("CSAConnector_oneToOne.svg")
plot2 = fig2.getroot()
plot2.moveto(430, 10)
txt2 = sg.TextElement(440, 20, "B", size=18, weight="bold")

fig3 = sg.fromfile("CSAConnector_mem_random(0.1).svg")
plot3 = fig3.getroot()
plot3.moveto(0, 325)
txt3 = sg.TextElement(10, 335, "C", size=18, weight="bold")

fig = sg.SVGFigure("9.65in", "7in")
fig.append([plot1, plot2, plot3])
fig.append([txt1, txt2, txt3])
fig.save("CSAConnector.svg")
