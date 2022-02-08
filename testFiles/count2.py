import csv
countyCases ={}
countyDeaths ={}
countyGeo={}
# todo: consider renaming this for clarity
# READS uscities.csv and matches all unique counties to coordinates
with open('uscities.csv','r',newline="") as citiesFile:
    cities=csv.reader(citiesFile)
    for line in cities:
        if not line[5] in countyGeo:       # if county is not already in countyGeo 
            lat=line[8]                    # add lat and long to countyGeo   
            lng=line[9]
            countyGeo[line[5]]=[lat,lng]    


# READS us_counties_covid19_daily.csv and adds daily deaths and cases 
with open('us_counties_covid19_daily.csv','r') as dataFile:
    data=csv.reader(dataFile)
    counter = 0
    flag=False
    for line in data:
        if(flag):
            if line[1] in countyCases:                      #if county already has recorded deaths and cases, add new daily deaths and cases to existing
                countyCases[line[1]]+=int(line[4])
                countyDeaths[line[1]]+=int(line[5])
            else:
                countyCases[line[1]]=int(line[4])           #for new counties, add new daily deaths and cases 
                countyDeaths[line[1]]=int(line[4])
        else:
            flag=True

# todo: rename results.csv for clarity?
# WRITES results.csv with 
with open('results.csv','w',newline="") as newFile:
    csvWriter=csv.writer(newFile,delimiter=',')
    for i in countyCases:
        if countyGeo.get(i) is not None:
            coords=countyGeo.get(i)
            print(i  +" "+  coords[0]+" "+coords[1])
        
        csvWriter.writerow([i]+[str(countyCases.get(i))]+[str(countyDeaths.get(i))]+[str(coords[0])]+[str(coords[1])])
