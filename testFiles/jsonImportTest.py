import json
from itertools import islice
import pandas as pd

file1 = open("myfile.json","r")
df = pd.read_csv('covid_dailies_total.csv')

test=file1.read() 

a=json.loads(test)

for index, row in islice(df.iterrows(), 0,None):
 fips=str(int(row['fips']))
 print("=====")
 print(fips)
 print(a[fips]['results'][0]['geometry']['location']['lat'])
 print(a[fips]['results'][0]['geometry']['location']['lng'])
 print("=====")