import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon

mycrs = 'EPSG:4269'
dbpath = '/Users/telliott/Library/CloudStorage/Dropbox/maps5/lewis_clark/'

def make_bbox(t):
    xmin,ymin,xmax,ymax = t
    poly = Polygon([(xmin,ymin),
        (xmax,ymin),(xmax,ymax),(xmin,ymax)])
    gs = gpd.GeoSeries(poly)
    bbox = gpd.GeoDataFrame({'geometry': gs})
    return bbox
    
t = -116, 44.9, -113, 46.8
bbox = make_bbox(t)
bbox = bbox.set_crs(mycrs)
LC = gpd.read_file(dbpath + 'doc.kml',
    driver='LIBKML')
LC = LC.to_crs(mycrs)
trail = LC.overlay(bbox,how='intersection')

fn = 'OR_WA_ID_MT_WY.shp.zip'
states = gpd.read_file(dbpath+fn)
states = states.to_crs(mycrs)
t = -118, 44.5, -112, 49
bbox = make_bbox(t)
bbox = bbox.set_crs(mycrs)
area = states.overlay(bbox,how='intersection')

ax = area.boundary.plot()
trail.plot(ax=ax,color='r')

'''
# show rows are unordered
for i,row in trail.iterrows():
    if i == 6:
        break
    pt = row['geometry'].representative_point()
    x,y,_ = pt.coords[:][0]
    plt.annotate(text=str(i),
        xy=(x,y),
        fontsize = 8)
'''

places = [{'name':'Lolo','x':-114.102778,'y':46.765278},
          {'name':'Lolo Pass','x':-114.58,'y':46.635},
          {'name':'Weippe','x':-115.939444,'y':46.377222},
          {'name':'Lemhi Pass','x':-113.445,'y':44.974167} ]
for loc in places:
    plt.scatter(x=loc['x'],y=loc['y'],
        s=20,zorder=2,color='k')

plt.savefig('Lemhi_Lolo.png',dpi=300)
