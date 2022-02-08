import csv
#todo: is this a duplicate of count2.py? figure out before commenting/adding to readme
with open('County Geodata.csv','r') as geoDataFile:
    geoData=csv.reader(geoDataFile)
    skip=False
    for line in geoData:
        if skip:
            with open('us_counties_covid19_daily.csv','r') as dataFile:
                data=csv.reader(dataFile)
                counter = 0
                flag=False
                for line2 in data:
                    if(flag):
                        if(str(line[1])==str(line2[1])):
                            counter+=int(line2[4])
                    else:
                        flag=True
                if not (counter==0):
                    print(line[1]+" "+str(counter))  
        else:
            skip=True

         