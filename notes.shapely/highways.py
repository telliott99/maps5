'''
illustrates clip
and a simple method to build a tilted bbox
for clipping highway data

currently the box isn't plotting on the geopandas plot
'''


import json, math, sys
import geopandas as gpd
import matplotlib.pyplot as plt

from shapely import plotting, Point, Polygon

dbpath = '/Users/telliott/data/'
with open(dbpath + 'cities.json') as fh:
    data = json.load(fh)

gdf = gpd.read_file(dbpath + 'I-5.shp.zip')


D = {}
for e in data:
    k = (e['city'],e['state'])
    D[k] = e
    
def get_xy(s):
    city, state = s.strip().split(',')
    e = D[(city.strip(),state.strip())]
    return ((e['longitude'],e['latitude']))
    
def build_clip_box(p,q,f=0.02):
    x1,y1 = p.x,p.y
    x2,y2 = q.x,q.y
    dx = x2-x1
    dy = y2-y1
    ddx = dy*f
    ddy = dx*f
    c1 = Point(x2-ddx,y2+ddy)
    c2 = Point(x2+ddx,y2-ddy)
    c3 = Point(x1+ddx,y1-ddy)
    c4 = Point(x1-ddx,y1+ddy)
    pg = Polygon([c1,c2,c3,c4])
    return pg

p = Point(get_xy('Los Angeles, California'))
q = Point(get_xy('San Jose, California'))
pg = build_clip_box(p,q)

plotting.plot_points([p,q])
plotting.plot_polygon(pg)
plt.savefig('out.png')
plt.close()

box = gpd.GeoDataFrame(
    {},geometry=[p,q,pg],crs=gdf.crs)

ax = box.plot()
sub = gdf.clip(pg)
sub.plot(ax,color='r')

mod = sys.argv[0].split('.')[0]
plt.savefig(mod + '.png')
