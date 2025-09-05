import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

path = '/Users/telliott/Programming/data/'
fn = 'western_states.shp.zip'
us_states = gpd.read_file(path+fn)

fn = 'North_America_Lakes_and_Rivers.zip'
fn = 'North_America_Lakes.zip'
na_rivers = gpd.read_file(path+fn)

#-----

ID = us_states['STATE'] == '16'
MT = us_states['STATE'] == '30'
OR = us_states['STATE'] == '41'
WA = us_states['STATE'] == '53'


sel = ID | MT | OR | WA
nw_states = us_states[sel]

######
# need to check crs for all
######


#-----

'''
I cannot find Flathead Lake by name in this dataset.
Idea:  make a bbox on the lake and use .cx
'''

xmax = -114.06
xmin = -114.15
ymax = 47.93
ymin = 47.81

sub = na_rivers.cx[xmin:xmax,ymin:ymax]

'''
>>> sub.iloc[0]
FID                                                      5027
Country                                                   USA
NameEn                                         Flathead River
NameEs                                           Río Flathead
NameFr                                         Flathead River
LengthKm                                              252.267
geometry    LINESTRING (-114.070420756334 48.4695088703562...
Name: 5026, dtype: object
>>> 
'''

xmin, ymin, xmax, ymax = -116, 47, -113, 49
from shapely.geometry import Polygon
poly = Polygon([(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)])

gs = gpd.GeoSeries(poly)
bbox = gpd.GeoDataFrame({'geometry': gs})

copy = bbox.set_crs('EPSG:4326')  # does not alter bbox
bbox = copy

sub = na_rivers.overlay(bbox, how='intersection')

fig,ax = plt.subplots(figsize=(7,7))

nw_states[MT].boundary.plot(ax=ax,
    color='gray',linewidth=0.5)
    
sub.plot(ax=ax,color='blue')

plt.savefig('/Users/telliott/Desktop/lakes.png')
