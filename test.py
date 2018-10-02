import requests
import json
import csv
import numpy as np
import pandas as pd

with open('./temp/config_json.json') as json_data_file: # structure: {"api_key" : "you_api_key"}
    data = json.load(json_data_file)

api_key = data["api_key"]

combinedUsers = {}

# This will be a loop that goes from 1 to 50, 10 search results each time (500 total results)
req = requests.get("https://api.rocketreach.co/v1/api/search'\?api_key="+api_key+"&location=montreal&keyword=human&start=3600")
req1 =requests.get("https://api.rocketreach.co/v1/api/search'\?api_key="+api_key+"&location=montreal&keyword=human&start=3610")

reqJson = req.json()
req1Json = req1.json()
# here we combine all the results into one list
combined_list = reqJson['profiles'] + req1Json['profiles']
print(combined_list)




# save to file
search_results = open('temp/SearchResults.csv', 'w+')

# create the csv writer object
csvwriter = csv.writer(search_results)
count = 0
for user in combined_list:

    if count == 0:

        header = user.keys()

        csvwriter.writerow(header)

        count += 1

    csvwriter.writerow(user.values())

search_results.close()




#open file in dataframe
SearchResultsDataframe= pd.read_csv('./temp/SearchResults.csv')


#loop through the list of profiles, for each profile, take the name and get the email permutations, for the company get the possible company domains


for index, row in SearchResultsDataframe.iterrows():
    name = row['name']
    company_name = row['current_employer']

   # name_permutations = NamePermutator(name) # TODO will give back a list of results in the form of justin.dumas or jdumas or dumas.j or j-dumas


    reqDomainNames = requests.get("https://autocomplete.clearbit.com/v1/companies/suggest?query=stripe") # TODO replace stripe with company_name
    reqJsonDomainNames = reqDomainNames.json() # this is a list in form
#  {
#    "name": "Segment",
#    "domain": "segment.com",
#    "logo": "https://logo.clearbit.com/segment.com"
#  },
#  {
#    "name": "Segmentify",
#    "domain": "segmentify.com",
#    "logo": "https://logo.clearbit.com/segmentify.com"
#  }


    #Then we combine all the possible combinations of name_permutations and domain names to get a list of around 200 possible emails for each person

