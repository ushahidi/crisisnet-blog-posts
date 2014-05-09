# Import the required modules into our environment
import requests
import pandas as pd

# Create a variable with your CrisisNET token.
token = '532d8dc4ed3329652f114b73' # REMOVE THIS BEFORE PUBLISHING

# Setup the request headers.
headers = {'Authorization': 'Bearer ' + token}

# Setup the request URL.
url = 'http://devapi.crisis.net/item?tags=%(tags)s&before=%(before)s&after=%(after)s&text=%(text)s&location=%(location)s&radius=%(radius)slimit=&%(limit)s&sources=%(sources)s&license=%(licenses)s'

# Create a list of filters (CHANGE THIS).
filters =   {'tags' : 'physical-violence,keyword2', # a list of keywords seperated by comma
             'after' : '2014-02-10T10:50:42.389Z', # a timestamp in ISO 8601 format
             'before' : '2014-02-10T10:50:42.389Z', # a timestamp in ISO 8601 format
             'text' : 'election+violence', # words seperated by a '+'
             'location' : '36.821946,-1.292066', # latitude and longitude
             'radius' : '10', # a number in meters
             'limit' : '100',
             'sources' : 'twitter,facebook',
             'licenses' : 'commercial'
            }

# Create the formatted pull URL.
formattedURL = url % filters

# Check the formatted pull URL.
print(formattedURL)

# Pull the data from CrisisNET.
r = requests.get(url, headers=headers)

# Check that the pull was successful.
print(r)

# Convert the pull's JSON into a pandas dataframe.
#df = pd.DataFrame(r.json())

# Print the dataframe.
#print(df)

# Save the dataframe as a csv
# df.to_csv('crisisnet_data_pull.csv')
