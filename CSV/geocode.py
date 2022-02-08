
import urllib.request
import json
import time


key="yourKey"


fips = ["123","333","12312","222","6566"]

searches=["Snohomish+County,Washington",
"Cook+County,Illinois",
"Orange+County,California",
"Maricopa+County,Arizona",
"Los+Angeles+County,California"]

flag=False

file1 = open("myfile.json","a")#append mode 
file1.write("{") #stuff



for i in range(len(searches)):
    address=searches[i]
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)
    # url = 'http://www.reddit.com/r/all/top/.json'
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req).read()
    # print(r)
    rr = json.loads(r)
    cont=json.dumps(rr)



    ##print formated
    #print (json.dumps(cont, indent=4, sort_keys=True))

    # print(cont)

    # Append-adds at last 
   
    print(cont)

    print(str(cont))

    if(flag):
        file1.write(",") #stuff
    else:
        flag=True
    file1.write("\""+fips[i]+"\":\n") #stuff

    file1.write(str(cont)) 
    
    
    time.sleep(1)
file1.write("}") #stuff
file1.close() 
# address="1600+Amphitheatre+Parkway,+Mountain+View,+CA"
# key="my-key-here"
# url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"
#  r = http.request('GET', url)