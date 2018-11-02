import os
import json

# read JSON file which is in the next parent folder
file = 'features.json'
json_data= open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# # connect to MySQL
# # # con = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = '',db = 'test',port ='3306')
# # # cursor = con.cursor()
# # #
# # #
# # # # parse json data to SQL insert

for i, item in enumerate(json_obj):
    name = validate_string(item.get("name", None))
    desc = validate_string(item.get("desc", None))
    klass = validate_string(item.get("class", None))
    print(klass.get('name'))
    description = ''
    for j in range(len(desc)):
        description += desc[j] + " "
#    print(description)
