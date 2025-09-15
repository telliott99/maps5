import geopandas as gpd
import matplotlib.pyplot as plt

dbpath = '/Users/telliott/data/'
hawaii = gpd.read_file(dbpath+
    'hawaii.shp.zip')

def save():
    plt.savefig('out.png',dpi=300)

#------

'''

The problem with the data for Hawaii is that it comes from a gdf of all the states.

So the names of the islands aren't included.
Getting to the individual POLYGON objects isn't easy.

hawaii.geometry is a GeoSeries
"A Series object designed to store shapely geometry objects."

iterating through geometries is undending
hawaii.geometry.get_geometry(0)
returns the item at index 0, wrapped in a new Series!'

islands = hawaii.geometry.explode(
    index_parts=True)
islands is a geopandas GeoSeries obj
with exactly the same problem

to get the actual objects you *can* use iloc
# getting to the MULTIPOLYGON
MP = hawaii.geometry.iloc[0]

'''

# 0 is the only valid index
MP = hawaii.geometry.iloc[0]
islands = list(MP.geoms)

# LINESTRING
#print(islands[0].boundary)

print(hawaii.geometry.geoms)



