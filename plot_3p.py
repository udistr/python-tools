import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.basemap import Basemap

def plot_3p(x, y, z, vmin1=np.nan, vmax1=np.nan, vmin2=np.nan, vmax2=np.nan, vmin3=np.nan, vmax3=np.nan, title1="a", title2="b", title3="c", xlabel="",cmap1='seismic', cmap2='seismic', cmap3='seismic',gm=np.nan):

  lon0=20
  ind=np.argmin(np.abs(x['lon']-lon0))

  ln=x.lon
  lt=x.lat

  ln=np.roll(ln,-ind)
  ln=np.where(ln<20,ln+360,ln) 
  x=np.roll(x,-ind,axis=1)
  y=np.roll(y,-ind,axis=1)
  z=np.roll(z,-ind,axis=1)

  if np.isnan(vmin1): vmin1=np.min(x) 
  if np.isnan(vmax1): vmax1=np.max(x) 

  if np.isnan(vmin2): vmin2=np.min(y) 
  if np.isnan(vmax2): vmax2=np.min(y) 

  if np.isnan(vmin3): vmin3=np.min(z) 
  if np.isnan(vmax3): vmax3=np.min(z) 
  
  fig = plt.figure(figsize=(13,9))
  gs = gridspec.GridSpec(2, 4)
  gs.update(wspace=0.05, hspace=0.05)
  m = Basemap(projection='cyl', resolution='c',lon_0=lon0+180)
  lon, lat = m(ln,lt)

  s=0.6
  fontsize=8

  #::::::::: coupled ::::::
  ax1=plt.subplot(gs[0,0:2])
  cs=m.pcolormesh(lon,lat,x,vmin=vmin1,vmax=vmax1,cmap=plt.get_cmap(cmap1),latlon=True)
  ax1.set_title(title1, loc='left')
  if (not np.all(np.isnan(gm))): ax1.set_title('mean='+str(gm[0]), loc='right')
  cbar=plt.colorbar(cmap=plt.get_cmap('rainbow'),shrink=s,spacing='proportional',orientation="horizontal",pad=0.07)
  cbar.ax.set_xlabel(xlabel,size=10,color='k')
  m.drawcoastlines()
  m.drawparallels(np.arange(-60.,90.,30.),labels=[1,0,0,0],textcolor='k',fontsize=fontsize)
  m.drawmeridians(np.arange(0.,360.,30.),labels=[0,0,0,1],textcolor='k',fontsize=fontsize)
  #m.bluemarble()
  plt.rc('xtick',labelsize=10)
  plt.rc('ytick',labelsize=10)
  #plt.annotate(date[i], xy=(0, 1),size=20,xycoords='axes fraction',color='w')

  #::::::::: Atmosphere
  ax2=plt.subplot(gs[0,2:4])
  cs=m.pcolormesh(lon,lat,y,vmin=vmin2,vmax=vmax2,cmap=plt.get_cmap(cmap2),latlon=True)
  ax2.set_title(title2, loc='left')
  if (not np.all(np.isnan(gm))): ax2.set_title('mean='+str(gm[1]), loc='right')
  cbar=plt.colorbar(cmap=plt.get_cmap('rainbow'),shrink=s,spacing='proportional',orientation="horizontal",pad=0.07)
  cbar.ax.set_xlabel(xlabel,size=10,color='k')
  m.drawcoastlines()
  m.drawparallels(np.arange(-60.,90.,30.),labels=[0,1,0,0],textcolor='k',fontsize=fontsize)
  m.drawmeridians(np.arange(0.,360.,30.),labels=[0,0,0,1],textcolor='k',fontsize=fontsize)
  #m.bluemarble()

  #::::::::: Atmosphere - coupled
  ax3=plt.subplot(gs[1,1:3])
  cs=m.pcolormesh(lon,lat,z,vmin=vmin3,vmax=vmax3,cmap=plt.get_cmap(cmap3),latlon=True)
  ax3.set_title(title3, loc='left')
  if (not np.all(np.isnan(gm))): ax3.set_title('mean='+str(gm[2]), loc='right')
  cbar=plt.colorbar(cmap=plt.get_cmap('seismic'),shrink=s,spacing='proportional',orientation="horizontal",pad=0.07)
  cbar.ax.set_xlabel(xlabel,size=10,color='k')
  m.drawcoastlines()
  m.drawparallels(np.arange(-60.,90.,30.),labels=[1,0,0,0],textcolor='k',fontsize=fontsize)
  m.drawmeridians(np.arange(0.,360.,30.),labels=[0,0,0,1],textcolor='k',fontsize=fontsize)
  #m.bluemarble()

  plt.tight_layout()


  return plt




