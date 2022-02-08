
import urllib.request
import json
import time
import pandas as pd
from itertools import islice

#controls
end=False
first=False
startIndex=2614
endIndex=None



df = pd.read_csv('covid_dailies_total.csv')
key="yourKey"

file1 = open("myfile.json","a")#append mode 
if first:
    file1.write("{") #stuff

flag=not first

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
         file1.write(",") #stuff
     else:
       flag=True
     file1.write("\""+str(fips)+"\":\n") #stuff
     file1.write(str(cont)) 
     print("====")
    
    
     time.sleep(.9)
if end:
    file1.write("}") #stuff
file1.close() 
