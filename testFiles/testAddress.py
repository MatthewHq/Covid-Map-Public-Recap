
import pandas as pd
from itertools import islice

df = pd.read_csv('covid_dailies_total.csv')
for index, row in islice(df.iterrows(), 2, 8):

     fips=int(row['fips'])
     print(fips)
     
     address = str(row['county']).replace(" ", "+") + "+county" + "+" + str(row['state'])
     print(address)
