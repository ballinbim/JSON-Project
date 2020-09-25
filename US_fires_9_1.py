import json

in_file = open('US_fires_9_1.json', 'r')

# out_file = open('readable_USfires_data.json', 'w')

fire_data = json.load(in_file)

# json.dump(fire_data, out_file, indent=4)

# lats = eq_data[0]
# lons = eq_data[1]
# brightness = eq_data[13]
list_of_fires = fire_data
#print(list_of_eqs[:])

print(type(list_of_fires))

print(len(list_of_fires)) 

lons,lats, brightness = [], [], []

for eq in list_of_fires:
    lon = eq[0,0]
    lat = eq[1,1]
    bright = eq[13,13]
    lons.append(lon)
    lats.append(lat)
    brightness.append(bright)

# print("Brightness")
print(lats) #first 10

# print("Lons")
# print(lons[:10])

# print("Lats")
# print(mags[:10])

# from plotly.graph_objs import Scattergeo, Layout
# from plotly import offline

# # data = [Scattergeo(lon=lons, lat=lats)]

# data = [{
#     'type': 'scattergeo',
#     'lon': lons,
#     'lat': lats,
#     'marker': {
#         'size':[5*mag for mag in mags],
#     }
# }]

# my_layout = Layout(title='Global Earthquakes')

# fig = {'data': data, 'layout':my_layout}

# offline.plot(fig, filename='global_earthquake.html')