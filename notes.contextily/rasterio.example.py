import matplotlib.pyplot as plt
import contextily as cx
import rasterio
import rasterio.plot

# note import needed for rasterio.plot

def get():
    w,s = -118.47,33.95
    e,n = -118.43,33.99
    img,ext = cx.bounds2raster(w,s,e,n,
        'out.tif',ll=True)

#get()

with rasterio.open("out.tif") as r:
    rasterio.plot.show(r)