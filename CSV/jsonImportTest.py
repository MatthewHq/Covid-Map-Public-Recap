

import json


file1 = open("myfile.json","r")

test=file1.read() 
# print(test)

a=json.loads(test)
print(a['123']['results'][0]['geometry']['location']['lat'])
# print(a

# print(a["results"]["0"]["types"])
# import json


# searches=["Snohomish+County,Washington",
# "Cook+County,Illinois",
# "Orange+County,California",
# "Maricopa+County,Arizona",
# "Los Angeles+County,California"]
# for i in range(1,len(searches)):
#     print(searches[i])
#     print("{"+"\"")


# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)
# print(y)