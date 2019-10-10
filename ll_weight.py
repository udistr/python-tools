import numpy as np

def ll_weight(lat,lon):

  pi=np.pi
  nlat=lat.shape[0]
  nlon=lon.shape[0]
  dlat=lat[1]-lat[0]  

  LAT=np.transpose(np.broadcast_to(lat,[nlon,nlat]))
  LON=np.broadcast_to(lon,[nlat,nlon])


  L=np.zeros(nlat+1)
  L[1:nlat]=np.linspace(90-dlat/2,-90+dlat/2,nlat-1)
  L[0]=90
  L[nlat]=-90
  L1=(L[0:nlat])/180*pi
  L2=(L[1:nlat+1])/180*pi
  w=np.transpose(np.broadcast_to(np.sin(L1)-np.sin(L2),[nlon,nlat]))
  w=w/np.sum(w)

  return w

