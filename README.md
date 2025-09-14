### A mapping project using geopandas

The polished version which works is a Jupyter Lab notebook.

The html versions of notebooks don't display well on github, but as local copies they are great.  OTOH, the notebooks do display there, but need to be opened by `jupyter lab mynb.ipynb` to display locally.

I made a record of what I tried as I went along, so much of what is here is just rambling notes.  I saved it all, just in case.

### Notebooks

- [exploring geopandas](explore.ipynb)
- missing points in [Pend Oreille](Pend_Oreille/Pend Oreille.ipynb)
- Pandas [cheatsheet](pandas/pandas.df.ipynb)

### Other points of note:

- Notes on the Lewis & Clark trail in the LC directory, including a map.

- [shapely](shapely.pdf)

See [nearest_points](nearest.py) for an example of obtaining the two nearest points in a lake and a river, then extracting those points from what's returned, building a new GeoDataFrame, and plotting the results.

See [shapely.pdf](shapely.pdf) for an example of working with a `Coordinate Sequence`.  