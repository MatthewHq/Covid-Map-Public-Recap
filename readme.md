# Covid-Map
ReactJS Map using Google Maps API, Mapbox, webpack, NodeJS to map out data aquired from [NY-Times (Raw Data)](https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv). The data was organized and processed using Pandas Python library and another Google Maps API subsection used to gather lat and long of a given county for the map points to be correctly projected.





## [aggregator.py](https://github.com/MatthewHoque/Covid-Map-Public-Recap/blob/main/aggregator.py)
daily script
    
* **READS** NY Times covid daily data from url - as df
* daily deaths and cases with fips, county, state
* **WRITES** df - as covid_dailies_total.csv
* **READS** covid_dailies_total.csv - as mainData

    * Aggregate cases and deaths based on fips, county, state
    * READS mapData.json and drop cols - as jsonMapData
        processed google geocoding API data with lat/lng/fips..
    * MERGES mainData and jsonMapData - as
    * WRITES combined - as covid_dailyCLEANED.csv
    * WRITES formatted fips, county, state, latitude, longitude, cases, and deaths for novel county entries to combinedData.json
* **tldr;** 
    * gets covid data, and processes a csv with a pretty format with the needed columns info(fips,state,county,lat/long,deaths/cases)
    * The idea was to run this intermittently which would add more county data as cases developed in new counties without needing to pull all the possible county lat/long info from the API as this would be costly in comparison to this "gather as you need" method

#### Finalized JSON data aggregated and processed from NY Times and Google Maps API can be found in [combinedData.json](https://github.com/MatthewHoque/Covid-Map-Public-Recap/blob/main/data/combinedData.json). This would be constantly changing on a day to day basis.


## [testFiles/testAddress.py](https://github.com/MatthewHoque/Covid-Map-Public-Recap/blob/main/testFiles/testAddress.py)
* test script

* READS covid_dailies_total.csv

* Designated range printing fips and formatting google geocode compatible location string
    

