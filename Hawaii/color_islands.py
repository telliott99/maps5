import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import sys

fig,ax = plt.subplots()

dbpath = '/Users/telliott/data/'
gdf = gpd.read_file(dbpath+
    'gz_2010_us_040_00_5m')
hawaii = gdf[gdf['NAME'] == 'Hawaii']

gs = hawaii.geometry
islands = gs.explode(index_parts=True)

names = ["Hawaii",
         "O'ahu",
         "Ni'ihau",
         "Kaua'i",
         "Molokai",
         "Kaho'olawe",
         "Maui",
         "Lanai",
         "Ford Island" ]   

ei = gpd.GeoDataFrame({},
    geometry = islands,
    crs = hawaii.crs)

ei['name'] = names
ei = ei[['name','geometry']]
ei.plot(cmap='Set2')

# not perfect, but you get the idea
def nudge(c,name):
    x,y = c.x,c.y
    if name == 'Hawaii':  x -= 0.2
    if name == 'Oahu':  y -= 0.1
    if name == "Ni'ihau":  y -= 0.1
    if name == "Kaua'i":  y += 0.1
    if name == 'Molokai':  x += 0.2; y += 0.1
    if name == "Kaho'olawe":  y -= 0.2
    if name == 'Maui':  x += 0.2; y -= 0.1
    if name == 'Lanai':  x -= 0.3; y -= 0.1
    if name == 'Ford Island':  x -= 0.4; y -= 0.4
    return x,y

for i,row in ei.iterrows():
    c = row.geometry.centroid
    xy = nudge(c,row['name'])
    plt.annotate(row['name'],xy=xy,) 

mod = sys.argv[0].split('.')[0]
plt.savefig(mod + '.png')