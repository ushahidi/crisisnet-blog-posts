import requests
import pandas as pd
import re

url = 'http://devapi.crisis.net/item?after=2014-03-10T10:50:42.389Z&limit=500'
token = '532d8dc4ed3329652f114b73'
headers = {'Authorization': 'Bearer ' + token}
r = requests.get(url, headers=headers)

df = pd.DataFrame(r.json())
print(df)



#


# def remove_non_ascii(s):
  #  return "".join(i for i in s if ord(i)<128)

# print(df.dtypes)
# types = df.apply(lambda x: pd.lib.infer_dtype(x.values))
# types[types=='unicode']
# df.apply(lambda x: pd.lib.infer_dtype(x.values))
# print(df.dtypes)

# Remove non-ascii characters from content field
# df['content'] = df['content'].apply(remove_non_ascii)

# Remove non-ascii characters from summary field
# df['summary'] = df['summary'].apply(remove_non_ascii)

# Remove non-ascii characters from geo field
# df['geo'] = df['geo'].apply(str)
# df['geo'] = df['geo'].apply(remove_non_ascii)
# df['geo'] = df['geo'].apply(remove_non_ascii)

# Remove non-ascii characters from tags field
# df['tags'] = df['tags'].apply(str)
# df['tags'] = df['tags'].apply(remove_non_ascii)

# print(df)
