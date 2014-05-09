import requests
import pandas as pd

url = 'http://devapi.crisis.net/item?source=reliefweb'
headers = {'Authorization': 'Bearer ' + '532d8dc4ed3329652f114b73'}

r = requests.get(url, headers=headers)

# Convert the pull's JSON into a pandas dataframe.
df = pd.DataFrame(r.json())

# Print the dataframe.
print(df)
