import requests
import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

file_path = "C:/Users/Noah/OneDrive/Documents/School/Fall-Semester-24/Programming-Logic-and-Design/M4-Mastery/L5/all_day.geojson.json"

with open(file_path, "r") as file:
    data = json.load(file)

earthquake_data = data["features"]
earthquake_locations = []
magnitudes = []

for earthquake in earthquake_data:
    coordinates = earthquake["geometry"]["coordinates"]
    magnitude = earthquake["properties"]["mag"]

    if coordinates and magnitude is not None:
        earthquake_locations.append((coordinates[0], coordinates[1]))
        magnitudes.append(magnitude)

plt.figure(figsize=(15, 10))
m = Basemap(projection='merc',
            llcrnrlat=-60, urcrnrlat=80,
            llcrnrlon=-180, urcrnrlon=180,
            resolution='c')

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray', lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

for (lon, lat), mag in zip(earthquake_locations, magnitudes):
    x, y = m(lon, lat)
    m.scatter(x, y, s=mag**2, c='red', alpha=0.6, edgecolors='k', zorder=5)

plt.title("Earthquake Activity (From Local File)")
plt.show()