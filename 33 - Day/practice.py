import requests


response = requests.get("https://api.github.com/search/repositories", params={"q": "requests+language:python"})
response.raise_for_status()

data = response.json()
items = data["items"]
first_item = items[0]
repo_name = first_item["name"]
print(repo_name)


print(response.headers)

print(response.headers["Accept"])
