import sys
import matplotlib.pyplot as plt
import geopandas as gpd

t = ' '.join(sys.argv[1:])

dbpath =  '/Users/telliott/Library/'
dbpath += 'CloudStorage/Dropbox/data/'
fn = 'OR_WA_ID_MT_WY_BC_AB_SK.shp.zip'
states = gpd.read_file(dbpath + fn)

mycrs = 'EPSG:4269'
states = states.to_crs(mycrs)

fn = 'nw_rivers.shp.zip'
nw_rivers = gpd.read_file(dbpath + fn)
nw_rivers = nw_rivers.to_crs(mycrs)

#-----------------------------------

sel = nw_rivers['NameEn'].str.contains(t)
gdf = nw_rivers[sel]

ax = states.boundary.plot(figsize=(9, 9),color='lightgray')

def report(e):
    D = e.to_dict()
    #print(D)
    name = D['NameEn']
    length = str(D['LengthKm'])
    country = D['Country']
    sL = [str(j) + ' ' + name,
          'LEN ' + length + ' km',
          'COUNTRY ' + country]
    print('\n'.join(sL))
    kL = ['NAME','PRENAME']
    for k in kL:
        if k in D:
            v = D[k]
            if v and v != 'None':
                if k == 'NAME':
                    print('STATE', v)
                if k == 'PRENAME':
                    print('PROVINCE', v)
    gs = D['geometry']
    print(gs.geom_type)
    xmin,ymin,xmax,ymax = gs.bounds
    print(round(xmin,2), round(ymin,2))
    print(round(xmax,2), round(ymax,2))
    print()

nrows,ncols = gdf.shape
for j in range(nrows):
    e = gdf.iloc[j]
    report(e)

ofn = '/Users/telliott/Desktop/ex.png'
plt.savefig(ofn,dpi=300)
