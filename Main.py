

# importing the requests library
import requests

# api-endpoint
URL = "https://api.github.com/orgs/"

print("\n\n")
print("****************Welcome**************")
print("\n")

#get org name from user
org_name = input("enter the organisations name to get its any 10 public repositories : ")
print("\n")
URL = URL + org_name +"/repos"


# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

if len(data) == 2:
    print("org has no public repo")
else:
    for i in range(0,10):
        print(data[i]["html_url"])
