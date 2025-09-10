import sys
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# 'STATE' attribute is a fips code as a string

fipsD = { 'AZ':'04','CA':'06','CO':'08',
          'ID':'16','MT':'30','NV':'32',
          'NM':'35','OR':'41','TX':'48',
          'UT':'49','WA':'53','WY':'56'}
          
# 'NAME' is just as you'd expect: 'Idaho', etc.

states = { 'AZ':'Arizona', 
           'CA':'California','CO':'Colorado',
           'ID':'Idaho',
           'MT':'Montana',
           'NM':'New Mexico','NV':'Nevada',
           'OR':'Oregon',
           'TX':'Texas',
           'UT':'Utah',
           'WA':'Washington','WY':'Wyoming' }

# 'PRENAME' is just as you'd expect: 'Alberta', etc.

provinces = {
           'BC':'British Columbia',
           'AB':'Alberta',
           'SK':'Saskatchewan' }

#---------

mycrs = 'EPSG:4326'

L = sys.argv
L.pop(0)
print(L)

if not L:
    print('usage: python mk_shapefile.py OR WA ID ...')
    sys.exit()

dbpath = '/Users/telliott/Library/CloudStorage/Dropbox/data/'
fn = 'gz_2010_us_040_00_5m.zip'
states_gdf = gpd.read_file(dbpath+fn)

fn = 'lpr_000b16a_e.zip'
provinces_gdf = gpd.read_file(
    dbpath+fn).to_crs(states_gdf.crs)


rL = []
for arg in L:
    if arg in states.keys():
        e = states[arg]
        sel = states_gdf['NAME'] == e
        rL.append(states_gdf[sel])      
    elif arg in provinces.keys():
        e = provinces[arg]
        sel = provinces_gdf['PRENAME'] == e
        rL.append(provinces_gdf[sel])    
    else:
        print('skipping unknown arg: %s' % arg)
        
result = pd.concat(rL)

ofn = '_'.join(L) + '.shp.zip'
result.to_file(
    filename=ofn,
    driver='ESRI Shapefile')


ax = result.boundary.plot(figsize=(9, 9),color='k')
ax.set_xlim(-130,-100)
ax.set_ylim(40,52.5)

ofn='/Users/telliott/Desktop/test.png'
plt.savefig(ofn, dpi=600)


