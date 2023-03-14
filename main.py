import requests
import validators

file1 = open('urls.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    if validators.url(line.strip()):
        response = requests.get(line.strip())
        print(line.strip(), response.status_code)
    elif validators.url("http://" + line.strip()):
        response = requests.get("http://" + line.strip())
        print("http://" + line.strip(), response.status_code)
    elif validators.url("http://www." + line.strip()):
        response = requests.get("http://www." + line.strip())
        print("http://www." + line.strip(), response.status_code)
    else:
        print(line.strip() + "is malformed.")
