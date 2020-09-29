import json

in_file = open('US_fires_9_14.json', 'r')

# out_file = open('readable_USfires_data.json', 'w')

fire_data = json.load(in_file)

# json.dump(fire_data, out_file, indent=4)

#print(list_of_eqs[:])
lons,lats, brightness = [], [], []

for fire in fire_data:
    lat = fire["latitude"]
    lon = fire["longitude"]
    bright = fire["brightness"]
    if bright > 450:
        lons.append(lon)
        lats.append(lat)
        brightness.append(bright)

# print("Latitude")
# print(lats[:10]) #first 10

# print("Longitude")
# print(lons[:10])

# print("Brightness")
# print(brightness[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = [Scattergeo(lon=lons, lat=lats, bright = brightness)]

data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'marker': {
        'size':[bright/100 for bright in brightness],
        'color':brightness,
        'colorscale':'viridis',
        'reversescale': True,
        'colorbar':{'title': 'Brightness'}
    }
    }]

my_layout = Layout(title='US Fires from 9-14-20 to 9-20-20')

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename='US Fires 9-14.html')