import re
try:
    import matplotlib
    matplotlib.use('Agg')
except:
    pass
import pylab
import numpy
import operator

colors = {"nest": "#ff6633", "PyNN": "#31cd32"}
styles = {"libcsa": "dotted", "csa": "solid"}

pylab.rc("axes", labelsize=12, titlesize=14)
pylab.rc("xtick", labelsize=12)
pylab.rc("ytick", labelsize=12)
pylab.rc("font", size=12)
pylab.rc("legend", fontsize=12)

datafile_runtime = "data/data_runtime.log"
with open(datafile_runtime) as f:
    rawdata = f.readlines()

data = {}
connectors = set()
for line in rawdata:

    d = line.split()

    # format is "pynn_comp CSAConnector connector library n nc time preptime itertime mem"
    # see the *_runtime.py scripts for details.
    pynn_component = d[0]
    connector = d[2]
    connectors.add(connector)
    library = d[3]
    n_neurons = int(d[4])
    n_connections = int(d[5])
    time = float(d[6])
    preptime = float(d[7])
    itertime = float(d[8])
    memory = int(d[9])

    try:
        data[connector][(pynn_component, library)].append((n_neurons, time, memory))
    except: # connector not in data, or (pynn_component, library) not in data[connector]
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

        arr = numpy.array(values)
        v = arr[arr[:,0].argsort()]
        n, t, m = v[:,0], v[:,1], v[:,2]
        color = colors[pynn_component]

        slope, _ = numpy.polyfit(numpy.log(n), numpy.log(t), 1)
        label = ", ".join((pynn_component, library, "%.2f" % slope))
        line, = ax1.loglog(n, t, lw=2, marker="o", ls="-",
                           label=label, color=color, zorder=i+100)
        if styles[library] == "dotted":
            line.set_dashes([2, 2])

        if "random" in connector:
            expected_t = [t[0]*(float(x)**2/n[0]**2) for x in n]
        else:
            expected_t = [t[0]*float(x)/n[0] for x in n]
        ax1.loglog(n, expected_t, lw=4, c=color, alpha=0.33, zorder=i)
        ax1.loglog(n, expected_t, lw=2, c="#eeeeee", zorder=i)

        if sum(m) != 0:
            slope, _ = numpy.polyfit(numpy.log(n), numpy.log(m), 1)
            label = ", ".join((pynn_component, library, "%.2f" % slope))
            line, = ax2.loglog(n, m/1024.0, lw=2, marker="o", ls="-",
                       label=label, color=color, zorder=i+100)
            if styles[library] == "dotted":
                line.set_dashes([2, 2])
     
            expected_m = [m[0]*float(x)/n[0]/1024. for x in n]
            ax2.loglog(n, expected_m, lw=4, c=color, alpha=0.33, zorder=i)
            ax2.loglog(n, expected_m, lw=2, c="#eeeeee", zorder=i)
    
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
               fancybox=True, loc="best", numpoints=1, handlelength=2.2)

    handles, labels = ax2.get_legend_handles_labels()
    if len(handles) != 0:
        hl = sorted(zip(handles, labels), key=operator.itemgetter(1))
        handles, labels = zip(*hl)
        ax2.legend(handles, labels, title="connector, library, slope",
                   fancybox=True, loc="best", numpoints=1, handlelength=2.2)

    fname = "CSAConnector_%s.svg" % connector
    fig1.savefig(fname)
    print "saved '%s'" % fname

    if len(handles) != 0:
        fname = "CSAConnector_mem_%s.svg" % connector
        fig2.savefig(fname)
        print "saved '%s'" % fname


for scaling_mode in ("weak", "strong"):

    datafile_runtime = "data/data_%s_scaling.log" % scaling_mode
    with open(datafile_runtime) as f:
        rawdata = f.readlines()
    
    data = {}
    connectors = set()
    for line in rawdata:
    
        d = line.split()

        # format is "pynn_comp CSAConnector connector library n nc time preptime itertime rank np
        # see the *_scaling.py scripts for details.
        pynn_component = d[0]
        connector = d[2]
        connectors.add(connector)
        library = d[3]
        n_neurons = int(d[4])
        n_connections = int(d[5])
        time = float(d[6])
        preptime = float(d[7])
        itertime = float(d[8])
        rank = int(d[9])
        np = int(d[10])
    
        if rank == 0:
            try:
                data[connector][(pynn_component, library)].append((n_neurons, time, np))
            except: # connector not in data, or (pynn_component, library) not in data[connector]
                try:
                    data[connector][(pynn_component, library)] = [(n_neurons, time, np)]    
                except: # connector not in data
                    data[connector] = {(pynn_component, library): [(n_neurons, time, np)]}
    
    for connector in connectors:
    
        fig1 = pylab.figure(figsize=(6,4))
        ax1 = fig1.add_subplot(1,1,1)
        ax1.yaxis.grid(color='gray', linestyle='dashed')
    
        for (i, ((pynn_component, library), values)) in enumerate(data[connector].items()):
    
            arr = numpy.array(values)
            v = arr[arr[:,2].argsort()]
            n, t, np = v[:,0], v[:,1], v[:,2]
            color = colors[pynn_component]

            slope, _ = numpy.polyfit(numpy.log(np), numpy.log(t), 1)
            label = ", ".join((pynn_component, library, "%.2f" % abs(slope)))
            line, = ax1.semilogy(np, t, lw=2, marker="o", ls="-", label=label,
                                  color=color, zorder=i+100)
            if styles[library] == "dotted":
                line.set_dashes([2, 2])

            if scaling_mode == "weak":
                expected_t = [t[0] for _ in np]
            else:
                expected_t = [t[0]*np[0]/float(x) for x in np]

            ax1.semilogy(np, expected_t, lw=4, c=color, alpha=0.33, zorder=i)
            ax1.semilogy(np, expected_t, lw=2, c="#eeeeee", zorder=i)
        
        fig1.subplots_adjust(left=0.14, bottom=0.1, right=0.96, top=0.91)
        
        ax1.set_title("%s scaling of CSAConnector(%s)" % (scaling_mode.capitalize(), connector))
        ax1.set_xlabel("number of processes")
        ax1.set_ylabel("wallclock time (s)")

        if scaling_mode == "strong":
            ax1.set_ylim([10**0, 10**5])

        ax1.set_xlim([1, 48])
        ax1.set_xticks([1, 2, 4, 6, 12, 24, 48])
    
        handles, labels = ax1.get_legend_handles_labels()
        hl = sorted(zip(handles, labels), key=operator.itemgetter(1))
        handles, labels = zip(*hl)
        ax1.legend(handles, labels, title="connector, library, slope",
                   fancybox=True, loc="best", numpoints=1, handlelength=2.2)
    
        fname = "CSAConnector_%s_scaling_%s.svg" % (scaling_mode, connector)
        fig1.savefig(fname)
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

fig3 = sg.fromfile("CSAConnector_strong_scaling_random(0.1).svg")
plot3 = fig3.getroot()
plot3.moveto(0, 325)
txt3 = sg.TextElement(10, 335, "C", size=18, weight="bold")

fig4 = sg.fromfile("CSAConnector_weak_scaling_random(0.1).svg")
plot4 = fig4.getroot()
plot4.moveto(430, 325)
txt4 = sg.TextElement(440, 335, "D", size=18, weight="bold")

fig = sg.SVGFigure("9.65in", "7in")
fig.append([plot1, plot2, plot3, plot4])
fig.append([txt1, txt2, txt3, txt4])
fig.save("CSAConnector.svg")
