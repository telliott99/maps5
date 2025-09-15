import geopandas as gpd
from shapely import LineString, Point, Polygon
from shapely.ops import nearest_points

def test():
    PG = Polygon([[2,2],[3,3],[2,4],[1,3],[2,2]])
    LS = LineString([(0,1),(1,1),(2,1),(3,1)])
    p = Point(2,2)
    
    print(PG.distance(p))
    print(nearest_points(PG,LS))

#test()

dbpath = '/Users/telliott/data/'

fn = 'North_America_Lakes_and_Rivers.zip'
na_rivers = gpd.read_file(dbpath + fn)
sel = na_rivers['NameEn'].str.contains("Pend Oreille")
po_river = na_rivers[sel]

fn = 'North_America_Lakes.zip'
na_lakes = gpd.read_file(dbpath+fn)
sel = na_lakes['NameEn'].str.contains('Pend Oreille')
po_lake = na_lakes[sel]

LS = po_river.iloc[1].geometry
PG = po_lake.iloc[0].geometry

result = nearest_points(
    LS, PG)
print(result)

'''
(maps) > python demo.py
(<POINT (-116.755 48.16)>, <POINT (-116.626 48.243)>)
(maps) > 
'''

# lemme just check
mind = 1e8
t = None

L1 = [(p) for p in LS.coords]
L2 = [(p) for p in PG.boundary.coords]
for p in LS.coords:
    for q in PG.boundary.coords:
        d = (p[0]-q[0])**2 + (p[1]-q[1])**2
        if d < mind:
            mind = d
            t = (p,q)

print(t[0])
print(t[1])

'''
(maps) > python nearest_demo.py
(<POINT (-116.755 48.16)>, <POINT (-116.626 48.243)>)
(-116.754568877487, 48.1599716677888)
(-116.625988077196, 48.2426547363217)
(maps) > 
'''
