import csv
countyCases ={}
countyDeaths ={}
countyGeo={}
# with open('County Geodata.csv','r') as geoDataFile:
#     geoData=csv.reader(geoDataFile)


#     skip=False
#     for line in geoData:
#         if skip:
#             counties[line[1]]=0
#         else:
#             skip=True


with open('uscities.csv','r',newline="") as citiesFile:
    cities=csv.reader(citiesFile)
    for line in cities:
        
        if not line[5] in countyGeo:
            lat=line[8]
            lng=line[9]
            countyGeo[line[5]]=[lat,lng]



with open('us_counties_covid19_daily.csv','r') as dataFile:
    data=csv.reader(dataFile)
    counter = 0
    flag=False
    for line in data:
        if(flag):
            if line[1] in countyCases:
                countyCases[line[1]]+=int(line[4])
                countyDeaths[line[1]]+=int(line[5])
            else:
                countyCases[line[1]]=int(line[4])
                countyDeaths[line[1]]=int(line[4])
            # counter+=int(line2[4])
        else:
            flag=True
    # if not (counter==0):
    #     print(line[1]+" "+str(counter))  
# print(counties)

with open('results.csv','w',newline="") as newFile:
    csvWriter=csv.writer(newFile,delimiter=',')
    for i in countyCases:
        if countyGeo.get(i) is not None:
            coords=countyGeo.get(i)
            print(i  +" "+  coords[0]+" "+coords[1])
        





        csvWriter.writerow([i]+[str(countyCases.get(i))]+[str(countyDeaths.get(i))]+[str(coords[0])]+[str(coords[1])])
