import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

dbpath = '/Users/telliott/Library/CloudStorage/Dropbox/data/'
fn = 'OR_WA_ID_MT_WY.shp.zip'
states = gpd.read_file(dbpath + fn)

#crs
albers = 'EPSG:9822'
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

#------------------------

ax = states.boundary.plot(figsize=(9, 9),color='k')

ctx.add_basemap(ax,crs=mycrs,
    source=ctx.providers.OpenTopoMap)

lw = 1.5

columbia.plot(ax=ax,color='red',linewidth=lw)
snake.plot(ax=ax,color='b',linewidth=lw) 
yellowstone.plot(ax=ax,color='red',linewidth=lw)
clark_fork.plot(ax=ax,color='b',linewidth=lw)
flathead.plot(ax=ax,color='b',linewidth=lw)
pend_oreille.plot(ax=ax,color='b',linewidth=lw) 
missouri.plot(ax=ax,color='magenta',linewidth=lw)
clearwater.plot(ax=ax,color='green',linewidth=lw)

flathead_lake.plot(ax=ax,color='cyan')
pend_oreille_lake.plot(ax=ax,color='cyan') 
yellowstone_lake.plot(ax=ax,color='magenta') 
fort_peck_lake.plot(ax=ax,color='cyan') 
canyon_ferry_lake.plot(ax=ax,color='cyan') 

ofn='/Users/telliott/Desktop/all+topo.png'
plt.savefig(ofn, dpi=600)
