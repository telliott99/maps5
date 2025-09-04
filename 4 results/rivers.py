# pulling it all together

import matplotlib.pyplot as plt
import geopandas as gpd
#import contextily as ctx

path = '/Users/telliott/Library/CloudStorage/Dropbox/data/'
fn = 'western_states.shp.zip'

us_states = gpd.read_file(path+fn)

ID = us_states['STATE'] == '16'
MT = us_states['STATE'] == '30'
OR = us_states['STATE'] == '41'
WA = us_states['STATE'] == '53'

sel = ID | MT | OR | WA
nw_states = us_states[sel]



#-----

# rivers and lakes
fn = 'North_America_Lakes_and_Rivers.zip'
na_rivers = gpd.read_file(path+fn)

fn = 'North_America_Lakes.zip'
na_lakes = gpd.read_file(path+fn)



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


sel = na_lakes['NameEn'].str.contains('Flathead')
flathead_lake = na_lakes[sel]


sel = na_lakes['NameEn'].str.contains('Pend Oreille')
pend_oreille_lake = na_lakes[sel]

'''

#-----

# this one is a mess

sel = na_rivers['NameEn'].str.contains('Missouri')
missouri = na_rivers[sel]

# arg is not modified
missouri = missouri.to_crs('EPSG:4269')

upper_missouri = missouri.overlay(
    nw_states[MT], how='intersection')

sel = na_rivers['NameEn'].str.contains("Bitterroot")
bitterroot = na_rivers[sel]
'''
#-----

fig,ax = plt.subplots(figsize=(7,7))

nw_states.boundary.plot(ax=ax,
    color='gray',linewidth=0.5)

#ctx.add_basemap(ax,source=ctx.providers.OpenTopoMap)
# issue with zoom level

lw = 1
    
columbia.plot(ax=ax, 
    color='r',linewidth=lw)
snake.plot(ax=ax, 
    color='b',linewidth=lw) 
yellowstone.plot(ax=ax, 
    color='r',linewidth=lw) 

clark_fork.plot(ax=ax, 
    color='b',linewidth=lw) 

flathead.plot(ax=ax, 
    color='b',linewidth=lw) 

pend_oreille.plot(ax=ax, 
    color='b',linewidth=lw) 



flathead_lake.plot(ax=ax,color='blue')

pend_oreille_lake.plot(ax=ax,color='blue')

'''

upper_missouri.plot(ax=ax, 
    color='purple',linewidth=lw)
     
    
flathead.plot(ax=ax, 
    color='red',linewidth=lw) 

bitterroot.plot(ax=ax, 
    color='blue',linewidth=lw) 
'''

ofn = '/Users/telliott/Desktop/rivers.png'
plt.savefig(ofn, dpi=300)

