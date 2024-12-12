import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

file_path = "C:/Users/Noah/OneDrive/Documents/School/Fall-Semester-24/Programming-Logic-and-Design/M4-Mastery/L5/modis_2023_United_States.csv"
fire_data = pd.read_csv(file_path)


latitudes = fire_data["latitude"]
longitudes = fire_data["longitude"]
brightness = fire_data["brightness"]

plt.figure(figsize=(15, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()

ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=":")
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.add_feature(cfeature.OCEAN, facecolor="aqua")

scatter = ax.scatter(
    longitudes, latitudes,
    c=brightness, cmap="hot", alpha=0.7, transform=ccrs.PlateCarree()
)

plt.colorbar(scatter, ax=ax, label="Fire Brightness")

plt.title("Global Fire Activity (Past 1 Day)", fontsize=16)

plt.show()
