import requests
import pandas as pd
import re
import json
import unicodedata

url = 'http://devapi.crisis.net/item?after=2014-02-10T10:50:42.389Z&limit=10'
token = '532d8dc4ed3329652f114b73'
headers = {'Authorization': 'Bearer ' + token}
r = requests.get(url, headers=headers)

df = pd.DataFrame(r.json())

df['content'] = df['content'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore'))
df['summary'] = df['summary'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore'))

print(df)

