import xarray as xr
from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import matplotlib.pyplot as plt

filename = 'omega500_hourly_tropics_2001.nc'
ds = xr.open_dataset(filename)

w = ds["w"]
lons = ds["longitude"]
lats = ds["latitude"]
time = ds["time"]
data = w[0,:,:]

# set the global font as Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.figure (figsize= (12, 6))
# create Basemap instance.
m = Basemap(projection='cyl',llcrnrlat=-30,urcrnrlat=30,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()
# draw parallels
parallels = np.arange(-30.,30.,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(-180.,170.,50.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

x, y = np.meshgrid(lons, lats)

# draw filled contours.
clevs = np.arange(-10, 4, 5)
cs = m.contourf(x, y, data)
# add colorbar.
cbar = m.colorbar(cs,location='right',pad="5%")
cbar.set_label('m/s')
# add title
plt.title('vertical velocity')
plt.savefig('vertical velocity.png', dpi=300)
plt.show()

# plot the time series of the vertical velocity at 0N, 0E
plt.figure(figsize=(12, 6))
plt.plot(time, w[:, 0, 0])
#add grid lines
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xlabel('time',fontsize=14)
plt.ylabel('vertical velocity', fontsize=14)
plt.savefig('vertical velocity time series.png', dpi=300)
plt.show()
