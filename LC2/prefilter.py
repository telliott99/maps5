import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

dbpath = '/Users/telliott/data/'
fn = 'OR_WA_ID_MT_WY.shp.zip'
states = gpd.read_file(dbpath + fn)

mycrs = 'EPSG:4269'
states = states.to_crs(mycrs)


fn = 'North_America_Lakes_and_Rivers.zip'
na_rivers = gpd.read_file(dbpath + fn)
na_rivers = na_rivers.to_crs(mycrs)
na_rivers = na_rivers.overlay(states, how='intersection')


fn = 'North_America_Lakes.zip'
na_lakes = gpd.read_file(dbpath+fn)
na_lakes = na_lakes.to_crs(mycrs)
na_lakes = na_lakes.overlay(states, how='intersection')

#------------------------

sel = na_rivers['NameEn'].str.contains('Columbia')
columbia = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains('Snake')
snake = na_rivers[sel]
sel = snake['LengthKm'] == 1591.5300
snake = snake[sel]

sel = na_rivers['NameEn'].str.contains('Yellowstone')
yellowstone = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains("Clark Fork")
clark_fork = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains("Flathead")
flathead = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains("Pend")
sub = na_rivers[sel]
sel = sub['LengthKm'] == 139.2460
pend_oreille = sub[sel]

sel = na_rivers['NameEn'].str.contains("Missouri")
sub = na_rivers[sel]
sel = sub['LengthKm'] == 2828.53
missouri = sub[sel]

sel = na_rivers['NameEn'].str.contains("Clearwater")
clearwater = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains("Bitterroot")
bitterroot = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains("Jefferson")
jefferson = na_rivers[sel]

sel = na_rivers['NameEn'].str.contains("Beaverhead")
beaverhead = na_rivers[sel]

gdf = pd.concat([columbia,snake,yellowstone,clark_fork,
                flathead,pend_oreille,missouri,clearwater,
                bitterroot,jefferson,beaverhead])
                
gdf.to_file('my_rivers.shp.zip',driver='ESRI Shapefile')

#----

sel = na_lakes['NameEn'].str.contains('Flathead')
flathead_lake = na_lakes[sel]

sel = na_lakes['NameEn'].str.contains('Pend Oreille')
pend_oreille_lake = na_lakes[sel]

sel = na_lakes['NameEn'].str.contains('Yellowstone')
yellowstone_lake = na_lakes[sel]

sel = na_lakes['NameEn'].str.contains('Fort Peck')
fort_peck_lake = na_lakes[sel]

sel = na_lakes['NameEn'].str.contains('Canyon Ferry')
canyon_ferry_lake = na_lakes[sel]

gdf = pd.concat([flathead_lake,pend_oreille_lake,yellowstone_lake,
                fort_peck_lake,canyon_ferry_lake])
gdf.to_file('my_lakes.shp.zip',driver='ESRI Shapefile')


