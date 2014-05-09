# Extracting Latitude and Longitude From CrisisNET Pulls

# Import the regex (re) package
import re
import pandas as pd

geo = pd.Series(["{'addressComponents': {'formattedAddress': 'Sundar Bajar, Lamjung'}, 'coords': [84.42, 28.132838]}",
                 "{'addressComponents': {'formattedAddress': 'Sundar Bajar, Lamjung'}, 'coords': [84.42, 28.132838]}",
                 "{'addressComponents': {'formattedAddress': 'Sundar Bajar, Lamjung'}, 'coords': [84.42, 28.132838]}",
                 "{'addressComponents': {'formattedAddress': 'Sundar Bajar, Lamjung'}, 'coords': [84.42, 28.132838]}",
                 "{'addressComponents': {'formattedAddress': ''}, 'coords': [-0.116667, 51.5]}",
                 "{'addressComponents': {'formattedAddress': ''}, 'coords': [-0.116667, 51.5]}",
                 "{'addressComponents': {'formattedAddress': ''}, 'coords': [-0.116667, 51.5]}"
                 ])

variables = dict(geo = geo)
df = pd.DataFrame(variables, columns = ['geo'])

print(df)

# Create a simple text string.
text = "{'addressComponents': {'formattedAddress': 'Sundar Bajar, Lamjung'}, 'coords': [84.42, 28.132838]}"

# re.search

# Find the longitude and latitude in the data string
longitude_re = re.search('\d{2}.\d{2}', text)
latitude_re = re.search(', \d{2}.\d{2}', text)

# Print the search results
print(longitude_re.group(), latitude_re.group())

# Convert the regex output into a float
longitude = float(longitude_re.group())
print(longitude)

# Convert the regex output into a float
latitude = float(latitude_re.group()[2:])
print(latitude)
