import requests
from bs4 import BeautifulSoup
import json

url = "https://github.com/Krishanu2206"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    # Get the user's name and bio
    name = soup.find("span", class_="p-name")
    bio = soup.find("div", class_="p-note")
    # Find the repositories tab link
    repo_tab = soup.find("a", {"href": lambda x: x and x.endswith("?tab=repositories")})
    repos_data = []
    if repo_tab:
        repos_url = "https://github.com" + repo_tab["href"]
        repos_response = requests.get(repos_url)
        if repos_response.status_code == 200:
            repos_soup = BeautifulSoup(repos_response.text, "html.parser")
            # Find all repository links
            repo_links = repos_soup.select('a[itemprop="name codeRepository"]')
            for a in repo_links:
                repo_name = a.text.strip()
                repo_url = "https://github.com" + a['href']
                # Try to fetch the README.md file from the main branch
                readme_url = f"{repo_url}/raw/main/README.md"
                readme_response = requests.get(readme_url)
                if readme_response.status_code != 200:
                    # Try master branch if main is not available
                    readme_url = f"{repo_url}/raw/master/README.md"
                    readme_response = requests.get(readme_url)
                readme_text = readme_response.text if readme_response.status_code == 200 else ""
                repos_data.append({
                    "repository": repo_name,
                    "readme": readme_text
                })
    data = {
        "name": name.text.strip() if name else None,
        "bio": bio.text.strip() if bio else None,
        "repositories": repos_data
    }
    print(json.dumps(data, indent=2))
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")