# testFiles/testAddress.py
    test script
    READS covid_dailies_total.csv
    Designated range printing fips and formatting google geocode compatible location string
    
# aggregator.py
    daily script
    
* **READS** NY Times covid daily data from url - as df
    * daily deaths and cases with fips, county, state
* **WRITES** df - as covid_dailies_total.csv
* **READS** covid_dailies_total.csv - as mainData

    Aggregate cases and deaths based on fips, county, state
    READS mapData.json and drop cols - as jsonMapData
        processed google geocoding API data with lat/lng/fips..
    MERGES mainData and jsonMapData - as
    WRITES combined - as covid_dailyCLEANED.csv
* **tldr;** 
    * gets covid data, and processes a csv with a pretty format with the needed columns info(fips,state,county,lat/long,deaths/cases)
