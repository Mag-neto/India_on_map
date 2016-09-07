#printing a part of India with Basemap
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv


longit=[]
lattit=[]
with open('path to lat-long', 'rb') as csvfile:
	file_info= csv.DictReader(csvfile,delimiter=' ')
	for row in file_info:
		longit.append(float(row['longitude']))
		lattit.append(float(row['lattitude']))

#fig=plt.figure(figsize=(20,10))
map = Basemap(llcrnrlon=59,llcrnrlat=5,urcrnrlon=98,urcrnrlat=37, resolution = 'h')

map.drawmapboundary(fill_color='aqua')
#Fill the continents with the color
#map.fillcontinents(color='#00CED1', lake_color='aqua')
map.bluemarble()
map.drawcoastlines()
map.readshapefile('Path to shape File', 'IND_adm1')
plt.title("Riots in India")

coordinates=zip(lattit,longit)
#for i in range(len(coordinates)):
	#x,y=coordinates[i]
	#map.plot(x,y,'ro',markersize=6)
x,y= map(longit,lattit)
map.plot(x,y,'ro',markersize=6)
plt.show()
