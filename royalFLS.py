import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
import plotnine
from tqdm import tqdm
import numpy as np

nonsoilcol = ["Elevation", "Aspect", "Slope", "Horizontal_Distance_To_Hydrology", "Vertical_Distance_To_Hydrology", "Horizontal_Distance_To_Roadways", "Hillshade_9am", "Hillshade_Noon", "Hillshade_3pm", "Horizontal_Distance_To_Fire_Points", "Wilderness_Area0", "Wilderness_Area1", "Wilderness_Area2", "Wilderness_Area3"]
soilcol = ["Soil_Type"+ str(x) for x in range(40)] # 40 soil type columns
covercol = nonsoilcol + soilcol
covercol.append("Cover_Type")
coverlabels = []

def main():
    print(matplotlib.__version__)
    sourcedf = pd.read_csv("covtype.data", names=covercol)
    #print(sourcedf.columns)
    #plt.plot(sourcedf["Cover_Type"], sourcedf["Elevation"], '.') #'o' means 'rings', '.' means 'points'
    #https://www.tutorialspoint.com/matplotlib/matplotlib_box_plot.htm
    print(sourcedf.shape)
    covertypes = []
    for i in tqdm(range(7)): #7 ground cover types, but now the numbers are off... (TODO: change from 4)
        covertypes.append(sourcedf["Elevation"].where(sourcedf["Cover_Type"] == i+1).dropna())

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) #what is [0,0,1,1]?
    print(covertypes)
    vp = ax.violinplot(covertypes)
    plt.xlabel('Trees')
    plt.ylabel('Elevation')
    plt.xticks()
    plt.show()



main()
