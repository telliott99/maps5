import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

fig,ax = plt.subplots()

dbpath = '/Users/telliott/data/'
hawaii = gpd.read_file(dbpath+
    'hawaii.shp.zip')

print(hawaii.shape)   # (1,6) a single row
gs = hawaii.geometry  # gs is a GeoSeries

mp = gs.iloc[0]    # mp is a MultiPolygon
p1 = mp.geoms[0]   # p1 is a Polygon
ext = p1.exterior  # ext is a LinearRing

# this plots all the islands the same color
# gdf.boundary.plot(ax=ax,cmap='magma')

# so dissolve the Multi collection
exp = hawaii.explode(index_parts=True)
print(exp.shape)   # (9,6) 9 islands

# we want to know which island is in each row
# a random point inside p1 (island of Hawaii)

D = {"Hawaii":[-155.519783,19.625055], 
     "Kaho'olawe":[-156.607857,20.550829],
     "Kauai":[-159.567160,22.017814],
     "Lanai":[-156.930387,20.834303],
     "Maui":[-156.279557,20.758340],
     "Molokai":[-156.986996,21.134644],
     "Ni'ihau":[-160.148047,21.904692],
     "O'ahu":[-157.968125,21.488976],
     "Ford Island":[-157.959627,21.363596]}

# each row of exp is a Series (not a Polygon)
def f(row):
    poly = row.geometry
    n = row.name[1]
    for k in D:
        xy = D[k]
        if poly.contains(Point(xy)):
            print(n,k)
        
exp.apply(f,axis=1)

'''
(maps) > python explore_hawaii.py 
(52, 6)
(288, 6)
0 Hawaii
2 Ni'ihau
3 Kauai
4 Molokai
5 Kaho'olawe
6 Maui
7 Lanai
8 O'ahu
8 Ford Island
(maps) >
'''