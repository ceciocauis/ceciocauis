from PyLTSpice import RawRead
import matplotlib.pyplot as plt         # use matplotlib for plotting the results
import numpy as np

"""
The following code receives as input .raw files, and plot V(out) vs frequency in log scale
This code plots the results for the Pad_tb testbench

"""

fig, ax = plt.subplots()


ax.set_xscale('log')
ax.grid(True)

#plt.xlim([0, 1000e12])              # Limit the X axis to just a subrange


files = []
response = ""

xdata = []
ydata = []

def plot(raw_file, position):
    # -----------Gets the data-----------
    raw = RawRead(raw_file)  # Read the RAW file contents from disk

    vout = raw.get_trace('db(out)')  # Get the second trace

    xdata.append(raw.get_axis())  # Get the X-axis data (time)
    ydata.append(vout.get_wave())  # Get all the values for the 'vout' trace

    # Do an X/Y plot on first subplot with blue color and axis labels
    ax.plot(xdata[position], ydata[position], color='#0000ff')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Vout/Vin (dB)')



def get():

    #-----------Plots the data-----------
    for indice, elemento in enumerate(files):
        plot(elemento,indice)

    plt.show()                              # Show matplotlib's interactive window with the plots




#-------------------------------
#Comment when running Rlayout_tb
while True:
    response = input("\nFiles for plotting, if not, write 0: ")
    if(response == "0"):
        break
    files.append(response)

get()



# get() 
