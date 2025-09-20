### A mapping project using geopandas

This repo contains a Jupyter Lab notebook about a mapping project.  We use GeoPandas to make maps of rivers and lakes in the Pacific Northwest.  The notebook is [here](explore/explore.ipynb).  There is a [pdf](explore.pdf).

I made a record of what I tried as I went along, so much of what is here is rambling notes.  I saved it all in folders labeled `notes.xxx`, just in case.

### Notebooks

- [exploring geopandas](explore/explore.ipynb)
- missing points in [Pend Oreille](Pend_Oreille/Pend_Oreille.ipynb)
- [Pandas cheatsheet](pandas/pandas.ipynb)
- [exploring Hawaii](Hawaii/hawaii.ipynb)

#### Why `ipynb`, `html` *and* `pdf`:

Locally, `html` versions of notebooks are a good way to display them, but on github, they do not render properly.  (to do:  figure out why).

Notebooks (`ipynb` files) *do* display nicely on github, but need to be opened by `jupyter lab mynb.ipynb` to display locally.  This isn't convenient when just browsing, since you can't just click on them.

#### Additionally:

- [notes](LC) on the Lewis & Clark trail, including a [map](LC_trail.png).
- the geometry module [shapely](notes.shapely/explore_shapely.ipynb)

See [here](Pend_Oreille/nearest.png) for an example of obtaining the two nearest points in a lake and a river, then extracting those points from what's returned, building a new GeoDataFrame, and plotting the results.