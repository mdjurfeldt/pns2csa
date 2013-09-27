import re
#import matplotlib
#matplotlib.use('Agg')
import pylab
import numpy
import operator

colors = {"nest": "#ff6633", "PyNN": "#31cd32"}
styles = {"libcsa": "--", "csa": "-"}

datafile = "data/data.log"
with open(datafile) as f:
    rawdata = f.readlines()

data = {}
connectors = set()
for line in rawdata:
    m = re.compile("(\S*) (.*): (\S*)").match(line)

    mode = m.group(1)
    time = float(m.group(3))
    params = m.group(2)[1:-1].split(", ")
    connector = params[0]
    connectors.add(connector)
    library = params[1]
    n_neurons = int(params[2][2:])

    try:
        data[connector][(mode, library)].append((n_neurons, time))
    except: # connector not in data, or (mode, library) not in data[connector]
        try:
            data[connector][(mode, library)] = [(n_neurons, time)]    
        except: # connector not in data
            data[connector] = {(mode, library): [(n_neurons, time)]}

fnames = []
for connector in connectors:
    fig = pylab.figure(figsize=(6,4))
    ax = fig.add_subplot(1,1,1)
    ax.yaxis.grid(color='gray', linestyle='dashed')

    for i, (key, values) in enumerate(data[connector].items()):
        v = numpy.sort(numpy.array(values),0)
        n, t = v[:,0], v[:,1]
        pynn_component = key[0].split(".")[0]
        color = colors[pynn_component]
        style = styles[key[1]]
        m, _ = numpy.polyfit(numpy.log(n), numpy.log(t), 1)
        label = ", ".join((pynn_component, key[1], "%.2f" % m))
        ax.loglog(n, t, lw=2, marker="o", linestyle=style, label=label, color=color, zorder=i+100)
        linear_t = [t[0]*float(x)/n[0] for x in n]
        ax.loglog(n, linear_t, lw=4, c="#dddddd", zorder=i)
        ax.loglog(n, linear_t, lw=2, c="#eeeeee", zorder=i)
    
    pylab.rc("axes", labelsize=14, titlesize=16)
    pylab.rc("xtick", labelsize=14)
    pylab.rc("ytick", labelsize=14)
    pylab.rc("font", size=14)
    pylab.rc("legend", fontsize=14)
#    pylab.rc("text", usetex=True)

    pylab.subplots_adjust(left=0.14, bottom=0.1, right=0.96, top=0.91)

    pylab.title(r"Run time of CSAConnector(%s)" % connector)
    pylab.xlabel("number of neurons")

    if "random" in connector:
        pylab.ylabel("wallclock time (s)")

    handles, labels = ax.get_legend_handles_labels()
    hl = sorted(zip(handles, labels), key=operator.itemgetter(1))
    handles2, labels2 = zip(*hl)
    ax.legend(handles2, labels2, title="connector, library, slope",
              fancybox=True, loc="best", numpoints=1)

    fname = "CSAConnector_%s.svg" % connector
    pylab.savefig(fname)
    fnames.append(fname)
    print "saved '%s'" % fname


import svgutils.transform as sg
import sys

#create new SVG figure
fig = sg.SVGFigure("9.65in", "3.5in")

# load matpotlib-generated figures
fig1 = sg.fromfile(fnames[0])
fig2 = sg.fromfile(fnames[1])

# get the plot objects
plot1 = fig1.getroot()
plot1.moveto(0, 10)
plot2 = fig2.getroot()
plot2.moveto(430, 10)

# add text labels
txt1 = sg.TextElement(10, 20, "A", size=18, weight="bold")
txt2 = sg.TextElement(440, 20, "B", size=18, weight="bold")

# append plots and labels to figure
fig.append([plot1, plot2])
fig.append([txt1, txt2])

# save generated SVG files
fig.save("CSAConnector.svg")
