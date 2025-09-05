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

#------------------------

ax = states.boundary.plot(figsize=(9, 9),color='lightgray')

ax.set_xlim(-130,-100)
ax.set_ylim(40,52.5)

#ctx.add_basemap(ax,crs=mycrs,source=ctx.providers.OpenTopoMap)

lw = 1

#------------------------

colorD = {'Columbia':'r',
          'Snake':'magenta',
          'Yellowstone':'r',
          'Missouri':'b',
          'Clark Fork':'magenta',
          'Flathead':'k',
          'Pend Oreille':'b',
          'Clearwater':'b',
          'Bitterroot':'b',
          'Jefferson':'orange',
          'Beaverhead':'magenta'  }

#------------------------

def do_filter(name,e):
    if name == 'Clearwater':
        return e[e['Country'] == 'USA']
    return e

def find_and_plot(name,kind='river'):
    if kind == 'river':
        gdf = nw_rivers
        color = colorD[name]
    else:
        gdf = nw_lakes
        color = 'blue'
    
    e = gdf[gdf['NameEn'].str.contains(name)]
    e = do_filter(name,e)
    e.plot(ax=ax,color=color,linewidth=lw)
    
for name in colorD.keys():
    find_and_plot(name)
    
lakes = ['Flathead','Yellowstone','Pend Oreille','Fort Peck',
         'Canyon Ferry']
for lake in lakes:
    find_and_plot(lake,kind='Lake')

ofn='/Users/telliott/Desktop/current.png'
plt.savefig(ofn, dpi=600)
