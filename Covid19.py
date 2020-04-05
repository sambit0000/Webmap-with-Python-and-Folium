# Importing the required libraries
import folium
import pandas as pd

# Loading the data
data = pd.read_csv('Coviddata.txt',sep=',')
# Removing null values
data.dropna(subset=['Lat', 'Long_','Deaths','Combined_Key'],inplace=True)

# Preparing the data
lat_list = list(data['Lat'])
long_list = list(data['Long_'])
deaths = list(data['Deaths'])
location_list = list(data['Combined_Key'])

# HTML to show hyperlink in poup
html = """
Location name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Deaths Reported: %s
"""

# Function to color code according to no of deaths
def color_producer(deaths):
    if deaths<=10:
        return 'green'
    elif deaths<=50:
        return 'blue'
    else:
        return 'red'

# Creating a basemap object
map = folium.Map(location=[28.70,77.10],zoom_start=3,tiles='Stamen Terrain')

# Creating a feature object
fg = folium.FeatureGroup(name='DeathCases')


for i,j,k,l in zip(lat_list,long_list,deaths,location_list):
    # Showing hyperlink in popup
    iframe = folium.IFrame(html=html % (l, l, k), width=200, height=100)
    # Creating a marker layer
    fg.add_child(folium.Marker(location = [i,j],popup= folium.Popup(iframe),icon = folium.Icon(color=color_producer(k))))


# Adding the feature object to the basemap object
map.add_child(fg)
# Saving the html file
map.save('Map2.html')


