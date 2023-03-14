import requests

file1 = open('urls.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    response = requests.get(line.strip())
    print(response.status_code)
