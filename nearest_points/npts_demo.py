import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

import shapely
import shapely.plotting
from shapely import affinity
from shapely.ops import nearest_points

pg = shapely.Polygon([(1,1),(3,1),(3,3),(1,3)])
rpg = affinity.rotate(pg, 15, 'center')
point = shapely.Point((6,3))
circle = point.buffer(1)

npts = nearest_points(rpg,circle)

fig, ax = plt.subplots()
plt.xlim(0,10)
plt.ylim(0,10)
plt.axis('equal')

shapely.plotting.plot_polygon(rpg,ax=ax)
shapely.plotting.plot_points(
    circle,ax=ax,lw=0.1)
shapely.plotting.plot_points(
    npts,ax=ax,color='r')

plt.savefig('out.png',dpi=300)
plt.close()

# npts is a tuple of shapely Point objects
X = [p.x for p in npts]
Y = [p.y for p in npts]
print(gpd.points_from_xy(X,Y))

'''
<GeometryArray>
[<POINT (2.992 2.16)>, <POINT (5.043 2.71)>]
Length: 2, dtype: geometry
(maps) > 
'''