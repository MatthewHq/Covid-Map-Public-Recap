import json
from itertools import islice
import pandas as pd


# READS myfile.json to get lat and long and combines with covid_dailies_total.csv into mapData.json

file1 = open("myfile.json","r")  #contains lat and long
file2 = open("mapData.json","a") #append mode 
df = pd.read_csv('covid_dailies_total.csv')
test=file1.read() 
a=json.loads(test)
file2.write("[\n") #opening bracket
for index, row in islice(df.iterrows(), 0,None):
    file2.write(" {") #stuff
    file2.write("\"fips\": " + str(int(row['fips'])) + ",\n")
    file2.write("  \"county\": \"" + row['county'] + "\",\n")
    file2.write("  \"state\": \"" + row['state'] + "\",\n")
    lat=a[str(int(row['fips']))]['results'][0]['geometry']['location']['lat']
    lng=a[str(int(row['fips']))]['results'][0]['geometry']['location']['lng']
    file2.write("  \"latitude\": " + str(lat) + ",\n")
    file2.write("  \"longitude\": " + str(lng) + ",\n")
    file2.write("  \"cases\": " + str(row['cases']) + ",\n")      #todo: check if these are being used and remove for redundancy 
    file2.write("  \"deaths\": " + str(row['deaths']) + "\n")     #todo: check if these are being used and remove for redundancy 
    file2.write(" }") #stuff
    if (df["fips"].iloc[-1]!=row['fips']):
        file2.write(",\n") 
file2.write("]") 
file1.close()
file2.close() 
