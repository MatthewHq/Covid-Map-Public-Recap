import pandas as pd

df = pd.read_csv('us_counties_covid19_daily.csv')

# print(df)
df = df.groupby(['fips','county','state']).agg({'deaths': 'sum', 'cases': 'sum'})
df.to_csv('covid_dailies_total.csv')

# print(grouped)

# coordinates = pd.read_csv('uscities.csv')
# coordinates=coordinates.drop_duplicates(subset='county_name',keep='first')
# coordinates=coordinates.rename(columns={'county_name': 'county'})
# coordinates = coordinates.groupby('county').agg({'lat':'mean','lng':'mean'})
# print(coordinates.head())
# coordinates=coordinates.rename(columns={'lat': 'latitude'})
# coordinates=coordinates.rename(columns={'lng': 'longitude'})

# print(coordinates)



# gc = coordinates.groupby('county_name')
# gc.drop_duplicates(subset=None, keep='first', inplace=False)

# coordinates = coordinates.drop(columns=['city','city_ascii','state_id', 'state_name', 'county_fips_all', 'county_name_all', 'population', 'density', 'source', 'military'
# , 'incorporated', 'timezone', 'ranking', 'zips', 'id','county_fips'])
# coordinates.to_csv('test.csv')

# print(coordinates)
# merged = df.merge(coordinates, on=['county'])
# merged = merged.groupby('county')
# print(merged)

# merged.to_json('covid_dailies_final.json',orient='records')


