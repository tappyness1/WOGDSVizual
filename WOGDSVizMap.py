# from mpl_toolkits.basemap import Basemap
# 
# m = Basemap(
#     projection='merc',
#     llcrnrlat=1.18506564,
#     urcrnrlat=1.50358105,
#     llcrnrlon=103.56674194,
#     urcrnrlon=104.03366089,
#     resolution='i'
# )
# m.drawmapboundary(fill_color='#85A6D9')
# m.drawcoastlines(color='#6D5F47', linewidth=.4)
# m.drawrivers(color='#6D5F47', linewidth=.4)
# m.fillcontinents(color='white',lake_color='aqua')
# plt.show()


# make bubbleplot with basemap
from mpl_toolkits.basemap import Basemap
longitudes = latlondf['Long'].tolist()
latitudes = latlondf['Lat'].tolist()
latlondf['Number of Posts'] =latlondf['Number of Posts']*10
sizes = latlondf['Number of Posts'].tolist()
agency = latlondf['Agencies'].tolist()

m = Basemap(
    projection='merc',
    llcrnrlat=1.18506564,
    urcrnrlat=1.50358105,
    llcrnrlon=103.56674194,
    urcrnrlon=104.03366089,
    resolution='i'
)
x, y = m(longitudes, latitudes)
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)
m.fillcontinents(color='white',lake_color='aqua')
m.scatter(x, y, s = sizes, zorder = 2, latlon = False, cmap = 'summer', color = 'm', )
plt.title("Number of Posts by Location")
overlaps = []
for label, x, y in zip(agency, x, y):
    print (label, x, y)
    if x in overlaps:
        plt.text(x + 100, y + 200, label)
    else:
        plt.text(x + 100, y - 200, label)
    overlaps.append(x)
plt.title("Posts by Agency")
plt.show()

latlondf['Number of Posts'] =latlondf['Number of Posts']/10
