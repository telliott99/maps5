import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

'''
Great Falls is about -111
Canadian border is 49

box -117 45 -111 49

Rivers
Flathead
Clark Fork
Bitterroot
Missouri
Jefferson
Beaverhead
Clearwater
Pend Oreille

Lakes
Flathead
Pend Oreille
Coeur d'Alene
Canyon Ferry

Points
Missoula
Plains
Thompson Falls

Lolo NF

LC Trail
Continental Divide
'''

mycrs = 'EPSG:4326'

# make the box
xmin = -117.5
ymin = 44.5
xmax = -109
ymax = 49

pg = Polygon([(xmin,ymin),(xmax,ymin),
                (xmax,ymax),(xmin,ymax)])
gs = gpd.GeoSeries(pg)
bbox = gpd.GeoDataFrame({'geometry': gs})
bbox = bbox.set_crs(mycrs)

def filter_and_crs(df):
    df = df.to_crs(mycrs)
    return df.overlay(bbox,how='intersection')

#-----

dbpath = '/Users/telliott/data/'

# states
states = gpd.read_file(dbpath + 
    'OR_WA_ID_MT_WY.shp.zip')

ID = states['NAME'] == 'Idaho'
MT = states['NAME'] == 'Montana'
states = states[ID | MT]
states = filter_and_crs(states)

#-----

# rivers and lakes
rivers = gpd.read_file(dbpath +
    'my_rivers.shp.zip')
rivers = filter_and_crs(rivers)

lakes = gpd.read_file(dbpath +
    'my_lakes.shp.zip')
lakes = filter_and_crs(lakes)
  
#-----

places = {'Lolo Pass':(-114.58,46.635),
          'Lemhi Pass':(-113.445,44.974167),
          'Missoula':(-113.996586,46.8787176),
          'Kalispell':(-114.338889,48.233889) }
          
          #'Bonners Ferry':(-116.319167,48.692778)

# National Forests and Parks

NF = gpd.read_file(dbpath +
    'BdyAdm_LSRS_AdministrativeForest.zip')
    
sel = NF['FORESTNAME'] == 'Lolo National Forest'
LoloNF = NF[sel]
    
#NP = gpd.read_file(dbpath +
    #'nps_boundary_shp.zip')
    
LC = gpd.read_file(dbpath + 'doc.kml',
    driver='LIBKML')
LC = filter_and_crs(LC)

divide = gpd.read_file(dbpath +
    'Continental_Divide-Pacific_Atlantic.zip')
divide = filter_and_crs(divide)

#-----

ax = states.boundary.plot(color='gray',lw=0.5)
LoloNF.plot(ax=ax,color='lightgray')

rivers.plot(ax=ax,color='b',lw=0.5,zorder=2)
lakes.plot(ax=ax,color='k',lw=0.5,zorder=2)
LC.plot(ax=ax,color='r',lw=1,zorder=1)

for t in places.values():
    ax.scatter(t[0],t[1],s=5,color='k',zorder=3)

divide.plot(ax=ax,color='orange',lw=0.5,zorder=2)

plt.savefig('out.png',dpi=300)

