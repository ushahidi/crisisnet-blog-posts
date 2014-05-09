import requests
import pandas as pd

url = 'http://devapi.crisis.net/item?tags=&sources='
token = '532d8dc4ed3329652f114b73'
headers = {'Authorization': 'Bearer ' + token}
r = requests.get(url, headers=headers)

df = pd.DataFrame(r.json())

print(df)

