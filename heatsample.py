import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from heatvalue import *

heat_values = np.array(heat_value)
textOn = True
isFahrenheit = False
tempMin = 20.0
tempMax = 28.0

def draw():
    global heat_values, tempMin, tempMax
    print(tempMin, tempMax)
    def toCelsius():
        global heat_values, tempMin, tempMax
        heat_values = (5/9)*(heat_values-32)
        tempMin = (5/9)*(tempMin-32)
        tempMax = (5/9)*(tempMax-32)
    def toFahrenheit():
        global heat_values, tempMin, tempMax
        heat_values = (9/5)*heat_values+32
        tempMin = (9/5)*tempMin+32
        tempMax = (9/5)*tempMax+32


    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)
    im = ax.imshow(heat_values, cmap='gray', vmin=tempMin, vmax = tempMax)

    cbar = ax.figure.colorbar(im, ax=ax, cmap='gray')
    cbar.ax.set_ylabel("Temperature", rotation=-90, va="bottom")

    # Loop over data dimensions and create text annotations.
    if textOn:
        for i in range(len(heat_values)):
            for j in range(len(heat_values[i])):
                text = ax.text(j, i, int(heat_values[i, j]),
                    ha="center", va="center", color="w")

    # Create sliders for different colored heatmaps
    heat_colors = ['gray', 'hot', 'plasma', 'inferno', 'magma', 'gnuplot', 'jet', 'rainbow']
    def update(val):
        print(scolor.val)
        im = ax.imshow(heat_values, cmap=heat_colors[scolor.val], vmin=tempMin, vmax=tempMax)
        #cbar = ax.figure.colorbar(im, ax=ax, cmap=heat_colors[scolor.val])
    axcolor = plt.axes([0.20, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    scolor = Slider(axcolor, 'Heatmaps', 0, len(heat_colors)-1, valinit=0, valstep=1)
    scolor.on_changed(update)

    # Turn Text on and off
    def textfunc(label):
        global textOn
        if label == 'Text On':
            print(label)
            textOn = True
        if label == 'Text Off':
            textOn = False
        draw()
    textrax = plt.axes([0.025, 0.65, 0.15, 0.15], facecolor='lightgoldenrodyellow')
    if textOn:
        textradio = RadioButtons(textrax, ('Text On', 'Text Off'), active=0)
    else:
        textradio = RadioButtons(textrax, ('Text On', 'Text Off'), active=1)
    textradio.on_clicked(textfunc)

    # Temperature buttons
    def tempfunc(label):
        global isFahrenheit, heat_values
        if label == 'Fahrenheit':
            toFahrenheit()
            isFahrenheit = True
        if label == 'Celsius':
            toCelsius()
            isFahrenheit = False
        draw()
    temprax = plt.axes([0.025, 0.35, 0.15, 0.15], facecolor='lightgoldenrodyellow')
    if isFahrenheit:
        tempradio = RadioButtons(temprax, ('Fahrenheit', 'Celsius'), active=0)
    else:
        tempradio = RadioButtons(temprax, ('Fahrenheit', 'Celsius'), active=1)
    tempradio.on_clicked(tempfunc)


    ax.set_title("Sample Heatmap")
    #fig.tight_layout()
    plt.show()

draw()