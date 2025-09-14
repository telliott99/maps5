'''
We're missing some points on the Pend Oreille River
right next to the Lake

Obtain them from Google Maps manually and add them.

'''

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely import Point, LineString

dbpath = '/Users/telliott/data/'
fn = 'North_America_Lakes_and_Rivers.zip'
na_rivers = gpd.read_file(dbpath + fn)

sel = na_rivers['NameEn'].str.contains("Pend Oreille")
po_river = na_rivers[sel]
print(po_river['LengthKm'])

#---------------

# we just copy the columns and entries from the original

D = {'FID':['4995'],
'Country':['USA'],
'NameEn':['Pend Oreille River'],
'NameEs':['Río Pend Oreille'],
'NameFr':['Pend Oreille River'],
'LengthKm':['15.632707'] }

df = pd.DataFrame(D)

#---------------

# the new points

s = '''
48.248589733216136, -116.64432444663814
48.256213458503204, -116.67112139993714
48.24972525370046, -116.68793039791562
48.23447473170333, -116.69304617990908
48.22360190290814, -116.69718752629615
48.209804691843075, -116.71643261093814
48.19194395801155, -116.71497095894
48.185122762281175, -116.71497095894
48.17618887113204, -116.7286130442559
48.167253423001256, -116.73738295624466
48.162541377351445, -116.74347317265425
48.16,-116.755'''

data = s.strip().split('\n')
X = []
Y = []

for e in data:
    t = e.strip().split(',')
    x = float(t[1])
    y = float(t[0])
    X.append(x)
    Y.append(y)

#---------------

# the geometry part
LS = LineString(zip(X,Y))

new_pts = gpd.GeoDataFrame(
    df,geometry=[LS],crs="EPSG:4326")
    
new_pts.to_file('po_addns.shp.zip', 
    driver='ESRI Shapefile')
    
ax = po_river.plot(color='k')
new_pts.plot(ax=ax,color='r')
plt.savefig('out.png',dpi=300)


'''
https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html

>>> po_river.iloc[1]
FID                                                      4995
Country                                                   USA
NameEn                                     Pend Oreille River
NameEs                                       Río Pend Oreille
NameFr                                     Pend Oreille River
LengthKm                                              139.246
geometry    LINESTRING (-116.754568877487 48.1599716677888...
Name: 4994, dtype: object
>>> 
'''