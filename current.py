import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

dbpath = '/Users/telliott/Library/CloudStorage/Dropbox/data/'
fn = 'OR_WA_ID_MT_WY_BC_AB_SK.shp.zip'
states = gpd.read_file(dbpath + fn)

#crs
albers = 'EPSG:9822'
mycrs = 'EPSG:4269'
states = states.to_crs(mycrs)


fn = 'nw_rivers.shp.zip'
nw_rivers = gpd.read_file(dbpath + fn)
nw_rivers = nw_rivers.to_crs(mycrs)

fn = 'nw_lakes.shp.zip'
nw_lakes = gpd.read_file(dbpath+fn)
nw_lakes = nw_lakes.to_crs(mycrs)

fn = 'Continental_Divide-Pacific_Atlantic.zip'
divide = gpd.read_file(dbpath+fn)
divide = divide.to_crs(mycrs)

#------------------------

ax = states.boundary.plot(figsize=(9, 9),color='lightgray')

ax.set_xlim(-130,-100)
ax.set_ylim(40,52.5)

divide.plot(ax=ax,color='r',lw=0.5)

#ctx.add_basemap(ax,crs=mycrs,source=ctx.providers.OpenTopoMap)

lw = 1

#------------------------

# it's probably better to filter for the data
# and check it in the interpreter

# note: cannot use == or is:
def sel(s):
    return nw_rivers['NameEn'].str.contains(s)

Columbia     = nw_rivers[sel('Columbia')]
Snake        = nw_rivers[sel('Snake')]
Yellowstone  = nw_rivers[sel('Yellowstone')]
Missouri     = nw_rivers[sel('Missouri')]
Clark_Fork   = nw_rivers[sel('Clark Fork')]
Pend_Oreille = nw_rivers[sel('Pend Oreille')]
Flathead     = nw_rivers[sel('Flathead')]
Clearwater   = nw_rivers[sel('Clearwater')]
Bitterroot   = nw_rivers[sel('Bitterroot')]
Jefferson    = nw_rivers[sel('Jefferson')]
Beaverhead   = nw_rivers[sel('Beaverhead')]

#------------------------

# do any clean up here

# Clearwater includes two rivers in BC

sel = Clearwater['Country'] == 'USA'
Clearwater = Clearwater[sel]

# Clearwater also has an odd nub
sel = Clearwater['LengthKm'] > 20
Clearwater = Clearwater[sel]

# Bitterroot has an odd nub

sel = Bitterroot['NameEn'] != 'Little Bitterroot River'
Bitterroot = Bitterroot[sel]

# Missouri contains left? fork

sel = Missouri['NameEn'] != 'Little Missouri River'
Missouri = Missouri[sel]

# other traces: S WY, NE MT

sel = Snake['NameEn'] != 'Snake Creek'
Snake = Snake[sel]

#------------------------

Flathead_L     = nw_lakes[nw_lakes['NameEn'].str.contains('Flathead')]
Yellowstone_L  = nw_lakes[nw_lakes['NameEn'].str.contains('Yellowstone')]
Pend_Oreille_L = nw_lakes[nw_lakes['NameEn'].str.contains('Pend Oreille')]
Fort_Peck_L    = nw_lakes[nw_lakes['NameEn'].str.contains('Fort Peck')]
Canyon_Ferry_L = nw_lakes[nw_lakes['NameEn'].str.contains('Canyon Ferry')]

#------------------------

Columbia.plot(ax=ax,color='r')
Yellowstone.plot(ax=ax,color='r')
Snake.plot(ax=ax,color='magenta')
Clark_Fork.plot(ax=ax,color='magenta')
Beaverhead.plot(ax=ax,color='magenta')

Missouri.plot(ax=ax,color='b')
Pend_Oreille.plot(ax=ax,color='b')
Clearwater.plot(ax=ax,color='b')
Flathead.plot(ax=ax,color='k')
Bitterroot.plot(ax=ax,color='k')
Jefferson.plot(ax=ax,color='k')


Flathead_L.plot(ax=ax,color='b')
Yellowstone_L.plot(ax=ax,color='r')
Pend_Oreille_L.plot(ax=ax,color='b')
Fort_Peck_L.plot(ax=ax,color='b')
Canyon_Ferry_L.plot(ax=ax,color='b')


ofn='/Users/telliott/Desktop/current.png'
plt.savefig(ofn, dpi=600)
