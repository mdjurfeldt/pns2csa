import svgutils.transform as sg

fig1 = sg.fromfile("finitem.svg")
plot1 = fig1.getroot()
plot1.moveto(0, 10)
txt1 = sg.TextElement(10, 20, "A", size=18, weight="bold")

fig2 = sg.fromfile("populations.svg")
plot2 = fig2.getroot()
plot2.moveto(430, 10)
txt2 = sg.TextElement(440, 20, "B", size=18, weight="bold")

fig3 = sg.fromfile("onetoone-new.svg")
plot3 = fig3.getroot()
plot3.moveto(0, 325)
txt3 = sg.TextElement(10, 335, "C", size=18, weight="bold")

fig4 = sg.fromfile("randnoself.svg")
plot4 = fig4.getroot()
plot4.moveto(430, 325)
txt4 = sg.TextElement(440, 335, "D", size=18, weight="bold")

fig = sg.SVGFigure("9.65in", "7in")
fig.append([plot1, plot2, plot3, plot4])
fig.append([txt1, txt2, txt3, txt4])
fig.save("csa-pane.svg")
