
import urllib.request
import json
import time
import pandas as pd
from itertools import islice

# Calls per fips googleAPI and collects raw data in bulk 
# controls for running file
end=False
first=False
startIndex=1698 
endIndex=1699

df = pd.read_csv('covid_dailies_total.csv')
key="yourKey"

file1 = open("myfile.json","a")#append mode 
if first:
    file1.write("{") 

flag=not first

# iterate through fips/counties and construct url then call googleAPI to get location of each
for index, row in islice(df.iterrows(), startIndex,endIndex):
     fips=int(row['fips'])
     address = str(row['county']).replace(" ", "+") + "+county" + "+" + str(row['state']).replace(" ", "+")
     print(address)
     url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)
     req = urllib.request.Request(url)
     r = urllib.request.urlopen(req).read()
     rr = json.loads(r)
     cont=json.dumps(rr)
     print(str(cont))
     if(flag):
         file1.write(",") 
     else:
       flag=True
     file1.write("\""+str(fips)+"\":\n") 
     file1.write(str(cont)) 
     print("====")
     time.sleep(.9)
if end:
    file1.write("}") 
file1.close() 
