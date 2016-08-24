import requests

# Set the request parameters
url = 'https://dev18537.service-now.com/api/now/table/incident'
user = raw_input()
pwd = raw_input()

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data='{"\
short_description":"Randomtest", "number":"some1234", "urgency":"1", "category":"software", "caller_id":"abel tuter"}')

# Check for HTTP codes other than 201
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data

print('Status:', response.status_code)
print('Headers:', response.headers)
print('Response:', str(response.json()))
