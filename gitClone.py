import os
import requests

# Put your github api token here
api_token = "*GITHUB_API_TOKEN*"

# Endpoint we'll be looking at
api_url = "https://api.github.com/orgs/*INSERT ORGANIZATION HERE*/repos"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {api_token}",
    "Accept": "application/vnd.github+json"
}

output_dir = "cloned_repos"
os.makedirs(output_dir, exist_ok=True)

page = 1
all_repos = []

while True:
    params = {"page": page, "per_page": 100}
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        repos = response.json()

        if not repos:
            break

        all_repos.extend(repos)

        page += 1
    else:
        print(f"Failed to retrieve repositories. Status code: {response.status_code}")
        break

# Clone each repository
for repo in all_repos:
    repo_name = repo["name"]
    repo_url = repo["clone_url"]

    os.system(f"git clone {repo_url} {output_dir}/{repo_name}")

print("Cloning completed.")
