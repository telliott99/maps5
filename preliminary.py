import sys,os
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

user = os.path.expanduser('~')
dbpath = user + '/data/'


fn = 'OR_WA_ID_MT_WY.shp.zip'
gdf = gpd.read_file(dbpath+fn)
OR = gdf[gdf['NAME'] == 'Oregon']
ID = gdf[gdf['NAME'] == 'Idaho']
