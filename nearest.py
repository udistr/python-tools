import numpy as np
# Define naive_fast that searches for the nearest model grid cell center
def nearest(latvar,lonvar,lat0,lon0):
    # Read latitude and longitude from file into numpy arrays
    latvals = latvar[:]
    lonvals = lonvar[:]
    dist_sq = (latvals-lat0)**2 + (lonvals-lon0)**2
    minindex_flattened = dist_sq.argmin()  # 1D index of min element
    x = np.unravel_index(minindex_flattened, latvals.shape)
    return x
