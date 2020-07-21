import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from heatvalue import *

heat_values = np.array(heat_value)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
im = ax.imshow(heat_values, cmap='hot', vmin=20.0, vmax = 28.0)

cbar = ax.figure.colorbar(im, ax=ax, 'hot')
cbar.ax.set_ylabel("Temperture (C)", rotation=-90, va="bottom")

# Loop over data dimensions and create text annotations.
for i in range(len(heat_values)):
    for j in range(len(heat_values[i])):
        text = ax.text(j, i, '',
                       ha="center", va="center", color="w")

# Create sliders for different colored heatmaps
heat_colors = ['gray', 'hot', 'plasma', 'inferno', 'magma', 'gnuplot', 'jet', 'rainbow']
def update(val):
    im = ax.imshow(heat_values, cmap=heat_colors[scolor.val], vmin=20.0, vmax=28.0)
    #cbar = ax.figure.colorbar(im, ax=ax, cmap=heat_colors[scolor.val])

axcolor = plt.axes([0.20, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')

scolor = Slider(axcolor, 'Heatmaps', 0, len(heat_colors)-1, valinit=0, valstep=1)
scolor.on_changed(update)


rax = plt.axes([0.025, 0.65, 0.15, 0.15], facecolor='lightgoldenrodyellow')
radio = RadioButtons(rax, ('Text On', 'Text Off'), active=1)
def textfunc(label):
    if label == 'Text On':
        for i in range(len(heat_values)):
            for j in range(len(heat_values[i])):
                text = ax.text(j, i, heat_values[i, j],
                            ha="center", va="center", color="w")
    if label == 'Text Off':
        for i in range(len(heat_values)):
            for j in range(len(heat_values[i])):
                text = ax.text(j, i, '',
                            ha="center", va="center", color="w")

radio.on_clicked(textfunc)


rax = plt.axes([0.025, 0.35, 0.15, 0.15], facecolor='lightgoldenrodyellow')
radio = RadioButtons(rax, ('Fahrenheit', 'Celsius'), active=1)
def textfunc(label):
    if label == 'Text On':
        for i in range(len(heat_values)):
            for j in range(len(heat_values[i])):
                text = ax.text(j, i, heat_values[i, j],
                            ha="center", va="center", color="w")
    if label == 'Text Off':
        for i in range(len(heat_values)):
            for j in range(len(heat_values[i])):
                text = ax.text(j, i, '',
                            ha="center", va="center", color="w")

radio.on_clicked(textfunc)


ax.set_title("Sample Heatmap")
#fig.tight_layout()
plt.show()