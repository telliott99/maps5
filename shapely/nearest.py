import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

from shapely import MultiPoint
from shapely.ops import nearest_points

dbpath = '/Users/telliott/data/'

fn = 'North_America_Lakes_and_Rivers.zip'
na_rivers = gpd.read_file(dbpath + fn)
sel = na_rivers['NameEn'].str.contains("Pend Oreille")
po_river = na_rivers[sel]

fn = 'North_America_Lakes.zip'
na_lakes = gpd.read_file(dbpath+fn)
sel = na_lakes['NameEn'].str.contains('Pend Oreille')
po_lake = na_lakes[sel]

#--------------------

river_geo = po_river.iloc[1].geometry # b/c CAN, USA
lake_geo = po_lake.geometry

np = nearest_points(river_geo,lake_geo)

'''
np is a 'tuple' object
cannot plot directly
np[0] is a 'geopandas.geoseries.GeoSeries'
np
>>> type(np)
<class 'tuple'>
>>> type(np[0])
<class 'geopandas.geoseries.GeoSeries'>
>>> print(np[0])
6229    POINT (-116.75457 48.15997)
Name: geometry, dtype: geometry
>>> type(np[0].iloc[0])
<class 'shapely.geometry.point.Point'>
'''

# extract the Point objects
L = [np[i].iloc[0] for i in range(len(np))]
MP = MultiPoint(L)

'''
# I thought this a better way:

X =  [float(p.x) for p in np]
Y =  [float(p.y) for p in np]

 FutureWarning: Calling float on a single element Series is deprecated and will raise a TypeError in the future. Use float(ser.iloc[0]) instead
 
L = gpd.points_from_xy(X,Y)
MP = MultiPoint(L)

'''

# construct a GeoDataFrame

D = { 'name':['nearest_points'] }
df = pd.DataFrame(D)

gdf = gpd.GeoDataFrame(df,
    geometry=[MP], 
    crs=po_river.crs)


ax = po_lake.plot()
gdf.plot(ax=ax,markersize=25,color='r',zorder=2)
plt.savefig('out.png',dpi=300)
