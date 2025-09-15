import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import sys

fig,ax = plt.subplots()

dbpath = '/Users/telliott/data/'
gdf = gpd.read_file(dbpath+
    'gz_2010_us_040_00_5m')
hawaii = gdf[gdf['NAME'] == 'Hawaii']
#print(hawaii)


gs = hawaii.geometry  # gs is a GeoSeries
islands = gs.explode(index_parts=True)
islands.boundary.plot(
    ax=ax)

L = list(range(9))

def f(p):
    #x,y = p.representative_point().coords[:][0]
    x = p.centroid.x
    y = p.centroid.y
    index = L.pop(0)
    plt.annotate(
        text=str(index),
        xy=(x,y))

islands.apply(f)   

'''
mp = gs.iloc[0]    # mp is a MultiPolygon

for i,p in islands:
    print(p)
    geom = p.geometry
    x,y = geom.representative_point().coords[:][0]
    plt.annotate(
        text=str(i),
        xy=(x,y))
'''

mod = sys.argv[0].split('.')[0]
plt.savefig(mod + '.png')
