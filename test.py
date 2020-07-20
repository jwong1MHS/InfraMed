import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from heatvalue import *

heat_values = np.array(heat_value)


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
im = ax.imshow(harvest, cmap='hot', vmin=20.0, vmax = 28.0)

# Loop over data dimensions and create text annotations.
for i in range(len(heat_values)):
    for j in range(len(harvest[i])):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

heat_colors = ['gray', 'hot', 'plasma', 'inferno', 'magma', 'gnuplot', 'jet', 'rainbow']
def update(val):
    im = ax.imshow(harvest, cmap=heat_colors[scolor.val], vmin=20.0, vmax = 28.0)

axcolor = plt.axes([0.20, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')

scolor = Slider(axcolor, 'Heatmaps', 0, len(heat_colors)-1, valinit=0, valstep=1)
scolor.on_changed(update)

ax.set_title("Sample Heatmap")
#fig.tight_layout()
plt.show()