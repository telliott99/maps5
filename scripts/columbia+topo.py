import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

dbpath = '/Users/telliott/Library/CloudStorage/Dropbox/data/'
fn = 'northwestUS.shp.zip'
gdf = gpd.read_file(dbpath + fn)

sub = gdf.to_crs('EPSG:3857')
ax = sub.boundary.plot(figsize=(9, 9))


fn = 'North_America_Lakes_and_Rivers.zip'
rivers = gpd.read_file(dbpath + fn)

sel = rivers['NameEn'].str.contains('Columbia')
columbia = rivers[sel]
columbia = columbia.to_crs('EPSG:3857')


ctx.add_basemap(ax,
    source=ctx.providers.OpenTopoMap)

columbia.plot(ax=ax, 
    color='red',linewidth=2)
    
ofn='/Users/telliott/Desktop/columbia+topo.png'
plt.savefig(ofn, dpi=300)
