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

'''
Last login: Mon Sep  8 13:03:15 on ttys000
/Users/telliott/.zshrc:cd:24: no such file or directory: Desktop
> activate
(maps) > python points.py 
MultiLineString
3 component LineStrings
LineString
221
(-115.99, 46.29) representative point
(-115.97, 46.3) first
(-116.0, 46.27) last
LineString
108
(-115.94, 46.32) representative point
(-115.97, 46.3) first
(-115.92, 46.33) last
LineString
14
(-115.91, 46.34) representative point
(-115.92, 46.33) first
(-115.91, 46.34) last

MultiLineString
2 component LineStrings
LineString
69
(-115.91, 46.35) representative point
(-115.91, 46.34) first
(-115.92, 46.37) last
LineString
82
(-115.96, 46.37) representative point
(-115.92, 46.37) first
(-116.0, 46.37) last

MultiLineString
11 component LineStrings
LineString
40
(-114.77, 46.51) representative point
(-114.76, 46.51) first
(-114.78, 46.51) last
LineString
1071
(-114.67, 46.52) representative point
(-114.76, 46.51) first
(-114.6, 46.58) last
LineString
24
(-114.77, 46.51) representative point
(-114.78, 46.51) first
(-114.76, 46.51) last
LineString
310
(-114.81, 46.54) representative point
(-114.78, 46.51) first
(-114.81, 46.58) last
LineString
61
(-114.59, 46.58) representative point
(-114.6, 46.58) first
(-114.59, 46.59) last
LineString
4
(-114.6, 46.59) representative point
(-114.6, 46.59) first
(-114.6, 46.59) last
LineString
220
(-114.6, 46.58) representative point
(-114.6, 46.59) first
(-114.6, 46.58) last
LineString
81
(-114.59, 46.59) representative point
(-114.6, 46.59) first
(-114.59, 46.59) last
LineString
3
(-114.59, 46.59) representative point
(-114.59, 46.59) first
(-114.59, 46.59) last
LineString
43
(-114.59, 46.59) representative point
(-114.59, 46.59) first
(-114.59, 46.59) last
LineString
257
(-114.59, 46.59) representative point
(-114.59, 46.6) first
(-114.59, 46.59) last

MultiLineString
17 component LineStrings
LineString
2
(-115.76, 46.29) representative point
(-115.76, 46.29) first
(-115.76, 46.29) last
LineString
1372
(-115.78, 46.3) representative point
(-115.76, 46.29) first
(-115.8, 46.31) last
LineString
3
(-115.76, 46.29) representative point
(-115.76, 46.29) first
(-115.76, 46.29) last
LineString
2
(-115.76, 46.29) representative point
(-115.76, 46.29) first
(-115.76, 46.29) last
LineString
3
(-115.76, 46.29) representative point
(-115.76, 46.29) first
(-115.76, 46.29) last
LineString
2
(-115.76, 46.29) representative point
(-115.76, 46.29) first
(-115.76, 46.29) last
LineString
3
(-115.8, 46.31) representative point
(-115.8, 46.31) first
(-115.8, 46.31) last
LineString
4
(-115.8, 46.31) representative point
(-115.8, 46.31) first
(-115.8, 46.31) last
LineString
1195
(-115.88, 46.33) representative point
(-115.86, 46.33) first
(-115.91, 46.34) last
LineString
2007
(-115.82, 46.32) representative point
(-115.86, 46.33) first
(-115.8, 46.31) last
LineString
67
(-115.91, 46.34) representative point
(-115.91, 46.34) first
(-115.91, 46.34) last
LineString
6011
(-115.66, 46.29) representative point
(-115.57, 46.34) first
(-115.76, 46.29) last
LineString
26
(-115.57, 46.34) representative point
(-115.57, 46.34) first
(-115.57, 46.34) last
LineString
1009
(-115.57, 46.35) representative point
(-115.57, 46.36) first
(-115.57, 46.34) last
LineString
42
(-115.57, 46.36) representative point
(-115.57, 46.36) first
(-115.57, 46.36) last
LineString
38
(-115.57, 46.36) representative point
(-115.57, 46.36) first
(-115.57, 46.36) last
LineString
923
(-115.55, 46.37) representative point
(-115.57, 46.36) first
(-115.53, 46.38) last

MultiLineString
2 component LineStrings
LineString
2881
(-114.77, 46.6) representative point
(-114.81, 46.58) first
(-114.73, 46.59) last
LineString
4283
(-114.66, 46.58) representative point
(-114.73, 46.59) first
(-114.59, 46.6) last

MultiLineString
2 component LineStrings
LineString
17
(-114.44, 46.77) representative point
(-114.44, 46.77) first
(-114.44, 46.77) last
LineString
296
(-114.37, 46.78) representative point
(-114.44, 46.77) first
(-114.3, 46.77) last

LineString
2585
(-114.56, 46.63) representative point
(-114.59, 46.6) first
(-114.55, 46.69) last

LineString
60
(-114.55, 46.69) representative point
(-114.55, 46.69) first
(-114.55, 46.7) last

LineString
30
(-115.49, 46.39) representative point
(-115.5, 46.39) first
(-115.49, 46.39) last

MultiLineString
32 component LineStrings
LineString
1041
(-115.35, 46.41) representative point
(-115.33, 46.42) first
(-115.38, 46.42) last
LineString
31
(-115.32, 46.42) representative point
(-115.32, 46.42) first
(-115.32, 46.42) last
LineString
364
(-115.31, 46.42) representative point
(-115.31, 46.42) first
(-115.3, 46.42) last
LineString
23
(-115.31, 46.42) representative point
(-115.32, 46.42) first
(-115.31, 46.42) last
LineString
24
(-115.31, 46.42) representative point
(-115.32, 46.42) first
(-115.31, 46.42) last
LineString
8
(-115.3, 46.42) representative point
(-115.3, 46.42) first
(-115.3, 46.42) last
LineString
7
(-115.3, 46.42) representative point
(-115.3, 46.42) first
(-115.3, 46.42) last
LineString
484
(-115.29, 46.43) representative point
(-115.29, 46.43) first
(-115.3, 46.42) last
LineString
1119
(-115.26, 46.44) representative point
(-115.29, 46.43) first
(-115.24, 46.45) last
LineString
2
(-115.29, 46.43) representative point
(-115.29, 46.43) first
(-115.29, 46.43) last
LineString
69
(-115.27, 46.44) representative point
(-115.27, 46.44) first
(-115.27, 46.44) last
LineString
21
(-115.24, 46.45) representative point
(-115.24, 46.45) first
(-115.24, 46.45) last
LineString
21
(-115.24, 46.45) representative point
(-115.24, 46.45) first
(-115.24, 46.45) last
LineString
1745
(-115.21, 46.45) representative point
(-115.24, 46.45) first
(-115.18, 46.47) last
LineString
18
(-115.17, 46.47) representative point
(-115.18, 46.47) first
(-115.17, 46.47) last
LineString
12
(-115.17, 46.47) representative point
(-115.18, 46.47) first
(-115.17, 46.47) last
LineString
6665
(-115.09, 46.53) representative point
(-115.17, 46.47) first
(-114.99, 46.55) last
LineString
8
(-114.99, 46.55) representative point
(-114.99, 46.55) first
(-114.99, 46.55) last
LineString
40
(-114.99, 46.55) representative point
(-114.99, 46.55) first
(-114.99, 46.55) last
LineString
17
(-114.99, 46.55) representative point
(-114.99, 46.55) first
(-114.99, 46.55) last
LineString
27
(-114.99, 46.55) representative point
(-114.99, 46.55) first
(-114.99, 46.55) last
LineString
21
(-114.99, 46.55) representative point
(-114.99, 46.55) first
(-114.99, 46.55) last
LineString
1410
(-114.97, 46.55) representative point
(-114.95, 46.56) first
(-114.99, 46.55) last
LineString
13
(-114.95, 46.56) representative point
(-114.95, 46.56) first
(-114.95, 46.56) last
LineString
16
(-114.95, 46.56) representative point
(-114.95, 46.56) first
(-114.95, 46.56) last
LineString
447
(-114.94, 46.56) representative point
(-114.93, 46.56) first
(-114.95, 46.56) last
LineString
14
(-114.93, 46.56) representative point
(-114.93, 46.56) first
(-114.93, 46.56) last
LineString
16
(-114.93, 46.56) representative point
(-114.93, 46.56) first
(-114.93, 46.56) last
LineString
22
(-114.93, 46.56) representative point
(-114.93, 46.56) first
(-114.93, 46.56) last
LineString
6
(-114.93, 46.56) representative point
(-114.93, 46.56) first
(-114.93, 46.56) last
LineString
7
(-114.93, 46.56) representative point
(-114.93, 46.56) first
(-114.93, 46.56) last
LineString
3846
(-114.87, 46.59) representative point
(-114.93, 46.56) first
(-114.81, 46.58) last

LineString
145
(-115.32, 46.42) representative point
(-115.32, 46.42) first
(-115.33, 46.42) last

MultiLineString
16 component LineStrings
LineString
670
(-115.51, 46.38) representative point
(-115.5, 46.39) first
(-115.52, 46.38) last
LineString
24
(-115.46, 46.4) representative point
(-115.46, 46.4) first
(-115.46, 46.4) last
LineString
58
(-115.46, 46.4) representative point
(-115.46, 46.4) first
(-115.46, 46.4) last
LineString
163
(-115.41, 46.41) representative point
(-115.4, 46.41) first
(-115.41, 46.41) last
LineString
7
(-115.4, 46.41) representative point
(-115.4, 46.41) first
(-115.4, 46.41) last
LineString
8
(-115.4, 46.41) representative point
(-115.4, 46.41) first
(-115.4, 46.41) last
LineString
1041
(-115.39, 46.42) representative point
(-115.4, 46.41) first
(-115.38, 46.42) last
LineString
19
(-115.41, 46.41) representative point
(-115.41, 46.41) first
(-115.41, 46.41) last
LineString
14
(-115.41, 46.41) representative point
(-115.41, 46.41) first
(-115.41, 46.41) last
LineString
42
(-115.41, 46.42) representative point
(-115.41, 46.41) first
(-115.41, 46.42) last
LineString
13
(-115.41, 46.42) representative point
(-115.41, 46.42) first
(-115.41, 46.42) last
LineString
17
(-115.41, 46.42) representative point
(-115.41, 46.42) first
(-115.41, 46.42) last
LineString
444
(-115.42, 46.42) representative point
(-115.41, 46.42) first
(-115.42, 46.42) last
LineString
34
(-115.42, 46.42) representative point
(-115.42, 46.42) first
(-115.42, 46.42) last
LineString
29
(-115.42, 46.42) representative point
(-115.42, 46.42) first
(-115.42, 46.42) last
LineString
1243
(-115.44, 46.41) representative point
(-115.42, 46.42) first
(-115.46, 46.4) last

LineString
562
(-115.32, 46.42) representative point
(-115.32, 46.42) first
(-115.33, 46.42) last

LineString
291
(-115.53, 46.38) representative point
(-115.53, 46.38) first
(-115.53, 46.38) last

LineString
3
(-115.53, 46.38) representative point
(-115.53, 46.38) first
(-115.53, 46.38) last

LineString
136
(-115.53, 46.38) representative point
(-115.53, 46.38) first
(-115.53, 46.38) last

LineString
44
(-115.91, 46.33) representative point
(-115.92, 46.33) first
(-115.91, 46.34) last

MultiLineString
2 component LineStrings
LineString
40
(-115.52, 46.38) representative point
(-115.53, 46.38) first
(-115.52, 46.38) last
LineString
1333
(-115.48, 46.39) representative point
(-115.46, 46.4) first
(-115.49, 46.39) last

LineString
340
(-115.49, 46.38) representative point
(-115.49, 46.39) first
(-115.5, 46.39) last

LineString
163
(-114.54, 46.71) representative point
(-114.55, 46.7) first
(-114.53, 46.73) last

LineString
295
(-114.5, 46.76) representative point
(-114.53, 46.73) first
(-114.44, 46.77) last

LineString
97
(-114.54, 46.71) representative point
(-114.55, 46.7) first
(-114.53, 46.73) last

(maps) > 
'''    