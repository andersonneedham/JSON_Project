import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# type of object
print(type(eq_data))

# number of earthquakes
list_of_eqs = eq_data["features"]
print(len(list_of_eqs))

print(type(list_of_eqs))


# create a list of
mags, lons, lats = [], [], []

for eqs in list_of_eqs:
    mag = eqs["properties"]["mag"]
    lon = eqs["geometry"]["coordinates"][0]
    lat = eqs["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(f"Magnitude: {mags[:10]}")
print(f"Longitude: {lons[:10]}")
print(f" Latitude: {lats[:10]}")

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

my_data = Scattergeo(lon=lons, lat=lats)
my_layout = Layout(title="Gloval Earthquakes")

fig = {"data": my_data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.htmml")
