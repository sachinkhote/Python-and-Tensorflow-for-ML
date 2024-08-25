import requests

username = "sachinkhote"

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"{username} has {len(data)} public repositories:")
    
    for repo in data:
        print(f"{repo['description']} \n")

else:
    print("Error Retrieving repository data.")
