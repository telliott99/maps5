import geopandas as gpd
import matplotlib.pyplot as plt

import utm
from pyproj import CRS


dbpath = '/Users/telliott/data/'

po_addns = gpd.read_file(
    dbpath + 'po_addns.shp.zip')
    

# to get length properly we must project to correct CRS

def utm_crs_from_latlon(lat, lon):
    crs_params = dict(
        proj = 'utm',
        zone = utm.latlon_to_zone_number(lat, lon),
        south = lat < 0
        )
    return CRS.from_dict(crs_params)

utm_crs = utm_crs_from_latlon(48.2,-116.6)
print(utm_crs) 

sub = po_addns.to_crs(utm_crs)
print(sub.geometry[0])
print(sub.length)

'''
+proj=utm +zone=11 +type=crs
LINESTRING (526404.0644849889 5343991.683102484, 524411.129314948 5344830.198400886, 523166.4076062218 5344103.82374203, 522793.4136110913 5342407.1919679, 522490.65436216904 5341197.455119945, 521066.9337879284 5339658.441673474, 521182.88584540464 5337673.630000758, 521185.69705673005 5336915.458459129, 520175.2114436488 5335918.793824149, 519526.6389227794 5334923.363112617, 519075.55416763667 5334398.095703166, 518219.3099086929 5334112.829505766)
0    15632.707337
dtype: float64


so that's in meters:  15.632 Km
sounds about right
'''