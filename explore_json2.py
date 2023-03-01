import json

infile = open("eq_data_30_day_m1.json", "r")
outfile = open("readable_eq_data2.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# type of object
print(type(eq_data))

# number of earthquakes
list_of_eqs = eq_data["features"]
print(len(list_of_eqs))

print(type(list_of_eqs))


# create a list of
mags, lons, lats, hover_text = [], [], [], []

for eqs in list_of_eqs:
    mag = eqs["properties"]["mag"]
    if mag > 5:
        lon = eqs["geometry"]["coordinates"][0]
        lat = eqs["geometry"]["coordinates"][1]
        title = eqs["properties"]["title"]

        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_text.append(title)

print(f"Magnitude: {mags[:10]}")
print(f"Longitude: {lons[:10]}")
print(f" Latitude: {lats[:10]}")

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# my_data = Scattergeo(lon=lons, lat=lats)

my_data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_text,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]
my_layout = Layout(title="Gloval Earthquakes")

fig = {"data": my_data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes2.htmml")
