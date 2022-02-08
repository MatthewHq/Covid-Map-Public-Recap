import pandas as pd
from itertools import islice
import requests
import io
import urllib.request
import time
import json

# READS nytimes covid daily data from url - as df
url="https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))
# todo: rename df 
# Aggregate cases and deaths based on fips, county, state
df = df.groupby(['fips','county','state']).agg({'deaths': 'sum', 'cases': 'sum'})

# WRITES df - as covid_dailies_total.csv
df.to_csv('covid_dailies_total.csv') #todo: potential redudancy from prior solution search

# READS mapData.json and drop cols - as jsonMapData
mainData = pd.read_csv('covid_dailies_total.csv', encoding='utf-8')
with open ('mapData.json', encoding = 'utf-8') as input: 
    fileString=input.read()
    jsonMapDat = pd.read_json(fileString+"]")
jsonMapDat=jsonMapDat.drop(columns=['county', 'state','cases','deaths'])

# MERGES mainData and jsonMapData - as combined
combined = pd.merge(mainData, jsonMapDat,how='left', on=['fips'])

# WRITES combined - as covid_dailies_totalCLEANED.csv
mainData.to_csv('covid_dailies_totalCLEANED.csv',encoding='utf-8-sig',index=False)

#debug =======
# print(combined[216:218])
# print("AAAAAAA")
# print(combined.iloc[217]['state'])
# combined.iloc[217]['state']="ueet"
# print(combined.iloc[217]['state'])
# print("AAAAAAA")

# WRITES formatted fips, county, state, latitude, longitude, cases, and deaths for novel county entries to combinedData.json
rowCounter=0
for index, row in islice(combined.iterrows(), 216,218):
    #if latitude and longitude do not exist for given FIPS (novel county entered), print error and add 
    if str(row['latitude'])=="nan" or str(row['longitude'])=="nan":
        fips=int(row['fips'])
        print(str(row['county'])+' '+str(row['state'])+' error: FIPS not included')
        key="yourKey"
        address = str(row['county']).replace(" ", "+") + "+county" + "+" + str(row['state']).replace(" ", "+")
        url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)
        print(url)
        req = urllib.request.Request(url)
        r = urllib.request.urlopen(req).read()
        rr = json.loads(r)
        mapDataFile = open("mapData.json","a") #append mode 
        mapDataFile.write(",\n {") 
        lat=rr['results'][0]['geometry']['location']['lat']
        lng=rr['results'][0]['geometry']['location']['lng']
        mapDataFile.write("\"fips\": " + str(int(row['fips'])) + ",\n")
        mapDataFile.write("  \"county\": \"" + row['county'] + "\",\n")
        mapDataFile.write("  \"state\": \"" + row['state'] + "\",\n")
        mapDataFile.write("  \"latitude\": " + str(lat) + ",\n")
        mapDataFile.write("  \"longitude\": " + str(lng) + ",\n")
        mapDataFile.write("  \"cases\": " + str(row['cases']) + ",\n")
        mapDataFile.write("  \"deaths\": " + str(row['deaths']) + "\n")
        mapDataFile.write("}")
        mapDataFile.close()
        time.sleep(.9)
    rowCounter+=1
print(combined[216:218])
combined.to_json('combinedData.json',orient='records')