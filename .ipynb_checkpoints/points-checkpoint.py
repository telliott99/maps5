import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon, LineString

mycrs = 'EPSG:4269'
dbpath = '/Users/telliott/Library/CloudStorage/Dropbox/maps5/lewis_clark/'

def make_bbox(t):
    xmin,ymin,xmax,ymax = t
    poly = Polygon([(xmin,ymin),
        (xmax,ymin),(xmax,ymax),(xmin,ymax)])
    gs = gpd.GeoSeries(poly)
    bbox = gpd.GeoDataFrame({'geometry': gs})
    return bbox
    
t = -116, 44.9, -114.3, 46.8
bbox = make_bbox(t)
bbox = bbox.set_crs(mycrs)
LC = gpd.read_file(dbpath + 'doc.kml',
    driver='LIBKML')
LC = LC.to_crs(mycrs)
trail = LC.overlay(bbox,how='intersection')

def f(sL):
    x,y,_ = sL
    return round(x,2),round(y,2)

# each feature has:  'id', 'type', 'property', 'geometry'
# 'type' is 'Feature', 'property' is html
# so geometry is the only useful thing


def analyze_LineString(coords):
    print('LineString')
    print(len(coords))

    # 'LineString' should have .representative_point()
    # but it doesn't
    # GeoSeries has one
    gs = gpd.GeoSeries(LineString(coords))
    rep_point = gs.representative_point()

    # rep_point is a shapely.coords.CoordinateSequence object
    # https://github.com/shapely/shapely/issues/984
    print(f(rep_point[0].coords[:][0]), 'representative point')
    
    print(f(coords[0]), 'first')
    print(f(coords[-1]), 'last')

def analyze_MultiLineString(geom):
    print('MultiLineString')
    L = geom['coordinates']
    print(len(L), 'component LineStrings')
    for coords in L:
        analyze_LineString(coords)

for e in trail.iterfeatures():    
    geom = e['geometry']    
    # geom has limited keys:  'type', 'coordinates'
    # 'type' is either 'LineString', 'MultiLineString'
    
    # if the type is 'MultiLineString'
    # then geom['coordinates'] is a tuple of tuples

    if geom['type'] == 'LineString':
        analyze_LineString(geom['coordinates'])
    else:
        analyze_MultiLineString(geom)
    print()
            