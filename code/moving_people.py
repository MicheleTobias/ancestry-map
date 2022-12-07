#GOAL: visualize ancestor movement data

# Tutorial: https://github.com/anitagraser/movingpandas-examples/blob/main/1-tutorials/1-getting-started.ipynb


# Import Libraries
import pandas as pd
import geopandas as gpd
import movingpandas as mpd


# load data from the csv in the data directory
    #df = pd.read_csv('../data/geolife_small.csv', delimiter=';')
    #df

df = pd.read_csv('../data/geolife_small.csv', delimiter=';')


# created the trajectory collection


#plot the trajectory collection