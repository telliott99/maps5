### A mapping project using geopandas

This repo contains a Jupyter Lab notebook about a mapping project.  We use GeoPandas to make maps of rivers and lakes in the Pacific Northwest.  The result is [explore](explore.pdf).

I made a record of what I tried as I went along, so much of what is here is rambling notes.  I saved it all, just in case.

#### Why `ipynb`, `html` *and* `pdf`:

Locally, `html` versions of notebooks are a good way to display them, but on github, they do not render properly.  (To do:  figure out why).

Notebooks *do* display nicely on github, but need to be opened by `jupyter lab mynb.ipynb` to display locally, which isn't convenient when just browsing.

### Notebooks

- [exploring geopandas](explore.ipynb)
- missing points in [Pend Oreille](Pend_Oreille/Pend Oreille.ipynb)
- Pandas [cheatsheet](pandas/pandas.df.ipynb)

#### Also:

- Notes on the Lewis & Clark trail [here](lewis_&_clark), including a map.
- exploring [shapely](shapely.pdf)

See [nearest_points](nearest.py) for an example of obtaining the two nearest points in a lake and a river, then extracting those points from what's returned, building a new GeoDataFrame, and plotting the results.

See [shapely.pdf](shapely.pdf) for an example of working with a `Coordinate Sequence`.  