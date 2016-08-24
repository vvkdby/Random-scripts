#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

# Set the request parameters
# this gives us a master list of which fields are available
#url = 'https://dev18537.service-now.com/api/now/table/sys_dictionary?sysparm_query=GOTOname%3Dincident'
url = 'https://dev18537.service-now.com/api/now/table/sys_choice?sysparm_query=element=subcategory&name=incident'
user = raw_input()
pwd = raw_input()
#34968cd28c331200a21c4f084b3f4f59
#75c779d74f5122003453b2718110c7fc
#https://dev18537.service-now.com/nav_to.do?uri=incident.do?sys_id=114b9a6b4f1522003453b2718110c797
#https://dev18537.service-now.com/nav_to.do?uri=sys_choice.do?sys_id=b0968cd28c331200a21c4f084b3f4f59
# Set proper headers
headers = {"Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
#print(''' 'Status:',response.status_code, 'Headers:',response.headers,''' 'Response:', str(response.json()))
#print('Cookies', response.cookies)
thejson = json.loads(response.text)

print json.dumps(thejson, indent=2, sort_keys=True)
