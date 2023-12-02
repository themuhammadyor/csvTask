import httpx
import csv
import json
import os

url = 'https://jsonplaceholder.typicode.com/users'
response = httpx.get(url=url)
data = response.json()

os.mkdir("users")
os.chdir("users")
for user in data:
  with open(f"{user['username']}.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(user.keys())
    csvwriter.writerow(user.values())