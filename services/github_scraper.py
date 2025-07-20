import requests
import httpx
from bs4 import BeautifulSoup
import json
import re
from typing import Optional, List, Dict, Any
from urllib.parse import urljoin, quote
import asyncio
from datetime import datetime

class GitHubScraper:
    def __init__(self):
        self.base_url = "https://github.com"
        self.api_base_url = "https://api.github.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def _make_request(self, url: str, timeout: int = 30) -> Optional[requests.Response]:
        """Make HTTP request with error handling"""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Request failed for {url}: {e}")
            return None

    def _parse_number(self, text: str) -> int:
        """Parse number from text, handling 'k', 'm' suffixes"""
        if not text:
            return 0
        text = text.strip().lower()
        if 'k' in text:
            return int(float(text.replace('k', '')) * 1000)
        elif 'm' in text:
            return int(float(text.replace('m', '')) * 1000000)
        else:
            return int(re.sub(r'[^\d]', '', text) or 0)

    def get_user_profile(self, username: str) -> Dict[str, Any]:
        """Scrape GitHub user profile"""
        url = f"{self.base_url}/{username}"
        response = self._make_request(url)
        
        if not response:
            return {"error": "Failed to fetch user profile"}

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract user information
        user_data = {"username": username}
        
        # Name
        name_elem = soup.find('span', class_='p-name')
        if name_elem:
            user_data['name'] = name_elem.text.strip()
        
        # Bio
        bio_elem = soup.find('div', class_='p-note')
        if bio_elem:
            user_data['bio'] = bio_elem.text.strip()
        
        # Location
        location_elem = soup.find('span', class_='p-label')
        if location_elem:
            user_data['location'] = location_elem.text.strip()
        
        # Company
        company_elem = soup.find('span', class_='p-org')
        if company_elem:
            user_data['company'] = company_elem.text.strip()
        
        # Avatar
        avatar_elem = soup.find('img', class_='avatar')
        if avatar_elem:
            user_data['avatar_url'] = avatar_elem.get('src')
        
        # Stats
        stats = soup.find_all('a', class_='Link--secondary')
        for stat in stats:
            text = stat.text.strip()
            if 'followers' in text.lower():
                user_data['followers'] = self._parse_number(text.split()[0])
            elif 'following' in text.lower():
                user_data['following'] = self._parse_number(text.split()[0])
        
        # Repository count
        repo_tab = soup.find('a', {'data-tab-item': 'repositories'})
        if repo_tab:
            repo_text = repo_tab.text.strip()
            user_data['public_repos'] = self._parse_number(re.findall(r'\d+', repo_text)[0] if re.findall(r'\d+', repo_text) else '0')
        
        return user_data

    def get_user_repositories(self, username: str, page: int = 1) -> List[Dict[str, Any]]:
        """Scrape user repositories"""
        url = f"{self.base_url}/{username}?tab=repositories&page={page}"
        response = self._make_request(url)
        
        if not response:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        repositories = []
        
        repo_list = soup.find_all('div', class_='col-10')
        for repo_div in repo_list:
            repo_link = repo_div.find('a', {'itemprop': 'name codeRepository'})
            if not repo_link:
                continue
                
            repo_name = repo_link.text.strip()
            repo_url = urljoin(self.base_url, repo_link['href'])
            
            # Description
            desc_elem = repo_div.find('p', {'itemprop': 'about'})
            description = desc_elem.text.strip() if desc_elem else None
            
            # Language
            lang_elem = repo_div.find('span', {'itemprop': 'programmingLanguage'})
            language = lang_elem.text.strip() if lang_elem else None
            
            # Stars, forks, etc.
            stars = 0
            forks = 0
            
            star_elem = repo_div.find('a', href=lambda x: x and 'stargazers' in x)
            if star_elem:
                stars = self._parse_number(star_elem.text.strip())
            
            fork_elem = repo_div.find('a', href=lambda x: x and 'forks' in x)
            if fork_elem:
                forks = self._parse_number(fork_elem.text.strip())
            
            # Get README content
            readme_content = self.get_repository_readme(username, repo_name)
            
            repositories.append({
                'name': repo_name,
                'full_name': f"{username}/{repo_name}",
                'description': description,
                'url': repo_url,
                'language': language,
                'stargazers_count': stars,
                'forks_count': forks,
                'readme_content': readme_content
            })
        
        return repositories

    def get_repository_info(self, username: str, repo_name: str) -> Dict[str, Any]:
        """Scrape detailed repository information"""
        url = f"{self.base_url}/{username}/{repo_name}"
        response = self._make_request(url)
        
        if not response:
            return {"error": "Repository not found"}

        soup = BeautifulSoup(response.text, 'html.parser')
        
        repo_data = {
            'name': repo_name,
            'full_name': f"{username}/{repo_name}",
            'url': url
        }
        
        # Description
        desc_elem = soup.find('p', class_='f4')
        if desc_elem:
            repo_data['description'] = desc_elem.text.strip()
        
        # Stats
        stats_elem = soup.find('div', id='repo-stats-counter')
        if stats_elem:
            # Stars
            star_elem = stats_elem.find('a', href=lambda x: x and 'stargazers' in x)
            if star_elem:
                repo_data['stargazers_count'] = self._parse_number(star_elem.text.strip())
            
            # Forks
            fork_elem = stats_elem.find('a', href=lambda x: x and 'forks' in x)
            if fork_elem:
                repo_data['forks_count'] = self._parse_number(fork_elem.text.strip())
        
        # Language
        lang_bar = soup.find('div', class_='BorderGrid-row')
        if lang_bar:
            lang_elem = lang_bar.find('span', class_='color-fg-default')
            if lang_elem:
                repo_data['language'] = lang_elem.text.strip()
        
        # Topics
        topics = []
        topic_elems = soup.find_all('a', class_='topic-tag')
        for topic in topic_elems:
            topics.append(topic.text.strip())
        repo_data['topics'] = topics
        
        # README
        repo_data['readme_content'] = self.get_repository_readme(username, repo_name)
        
        # Languages
        repo_data['languages'] = self.get_repository_languages(username, repo_name)
        
        return repo_data

    def get_repository_readme(self, username: str, repo_name: str) -> Optional[str]:
        """Get repository README content"""
        readme_urls = [
            f"https://raw.githubusercontent.com/{username}/{repo_name}/main/README.md",
            f"https://raw.githubusercontent.com/{username}/{repo_name}/master/README.md",
            f"https://raw.githubusercontent.com/{username}/{repo_name}/main/readme.md",
            f"https://raw.githubusercontent.com/{username}/{repo_name}/master/readme.md"
        ]
        
        for url in readme_urls:
            response = self._make_request(url)
            if response and response.status_code == 200:
                return response.text
        
        return None

    def get_repository_languages(self, username: str, repo_name: str) -> Dict[str, int]:
        """Scrape repository languages"""
        url = f"{self.base_url}/{username}/{repo_name}"
        response = self._make_request(url)
        
        if not response:
            return {}

        soup = BeautifulSoup(response.text, 'html.parser')
        languages = {}
        
        # Find language stats
        lang_section = soup.find('div', class_='BorderGrid-row')
        if lang_section:
            lang_links = lang_section.find_all('a', class_='d-inline-flex')
            for link in lang_links:
                lang_name = link.find('span', class_='color-fg-default')
                lang_percent = link.find('span', class_='percent')
                
                if lang_name and lang_percent:
                    name = lang_name.text.strip()
                    percent = float(lang_percent.text.strip().replace('%', ''))
                    languages[name] = percent
        
        return languages

    def get_repository_commits(self, username: str, repo_name: str, page: int = 1) -> List[Dict[str, Any]]:
        """Scrape repository commits"""
        url = f"{self.base_url}/{username}/{repo_name}/commits?page={page}"
        response = self._make_request(url)
        
        if not response:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        commits = []
        
        commit_groups = soup.find_all('div', class_='TimelineItem-body')
        for group in commit_groups:
            commit_links = group.find_all('a', class_='Link--primary')
            for link in commit_links:
                commit_url = urljoin(self.base_url, link['href'])
                commit_sha = link['href'].split('/')[-1]
                commit_message = link.text.strip()
                
                # Get author and date
                author_elem = group.find('a', class_='commit-author')
                author = author_elem.text.strip() if author_elem else None
                
                date_elem = group.find('relative-time')
                date = date_elem.get('datetime') if date_elem else None
                
                commits.append({
                    'sha': commit_sha,
                    'message': commit_message,
                    'author': author,
                    'date': date,
                    'url': commit_url
                })
        
        return commits

    def get_repository_issues(self, username: str, repo_name: str, state: str = 'open') -> List[Dict[str, Any]]:
        """Scrape repository issues"""
        url = f"{self.base_url}/{username}/{repo_name}/issues?q=is:issue+is:{state}"
        response = self._make_request(url)
        
        if not response:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        issues = []
        
        issue_items = soup.find_all('div', class_='Box-row')
        for item in issue_items:
            title_elem = item.find('a', class_='Link--primary')
            if not title_elem:
                continue
            
            title = title_elem.text.strip()
            issue_url = urljoin(self.base_url, title_elem['href'])
            issue_number = int(title_elem['href'].split('/')[-1])
            
            # Get author
            author_elem = item.find('a', class_='Link--muted')
            author = author_elem.text.strip() if author_elem else None
            
            # Get labels
            labels = []
            label_elems = item.find_all('a', class_='IssueLabel')
            for label in label_elems:
                labels.append(label.text.strip())
            
            issues.append({
                'number': issue_number,
                'title': title,
                'state': state,
                'author': author,
                'labels': labels,
                'url': issue_url
            })
        
        return issues

    def get_organization_info(self, org_name: str) -> Dict[str, Any]:
        """Scrape organization information"""
        url = f"{self.base_url}/{org_name}"
        response = self._make_request(url)
        
        if not response:
            return {"error": "Organization not found"}

        soup = BeautifulSoup(response.text, 'html.parser')
        
        org_data = {"name": org_name}
        
        # Display name
        name_elem = soup.find('h1', class_='h2')
        if name_elem:
            org_data['display_name'] = name_elem.text.strip()
        
        # Description
        desc_elem = soup.find('div', class_='f4')
        if desc_elem:
            org_data['description'] = desc_elem.text.strip()
        
        # Location
        location_elem = soup.find('span', class_='p-label')
        if location_elem:
            org_data['location'] = location_elem.text.strip()
        
        # Website
        website_elem = soup.find('a', class_='Link--primary')
        if website_elem:
            org_data['blog'] = website_elem.get('href')
        
        # Avatar
        avatar_elem = soup.find('img', class_='avatar')
        if avatar_elem:
            org_data['avatar_url'] = avatar_elem.get('src')
        
        return org_data

    def search_repositories(self, query: str, sort: str = 'stars', order: str = 'desc') -> List[Dict[str, Any]]:
        """Search GitHub repositories"""
        url = f"{self.base_url}/search?q={quote(query)}&type=Repositories&s={sort}&o={order}"
        response = self._make_request(url)
        
        if not response:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        repositories = []
        
        repo_items = soup.find_all('div', class_='f4')
        for item in repo_items:
            repo_link = item.find('a')
            if not repo_link:
                continue
            
            repo_url = urljoin(self.base_url, repo_link['href'])
            repo_parts = repo_link['href'].strip('/').split('/')
            
            if len(repo_parts) >= 2:
                username, repo_name = repo_parts[0], repo_parts[1]
                
                repositories.append({
                    'name': repo_name,
                    'full_name': f"{username}/{repo_name}",
                    'url': repo_url,
                    'owner': username
                })
        
        return repositories

    def get_trending_repositories(self, language: str = '', since: str = 'daily') -> List[Dict[str, Any]]:
        """Get trending repositories"""
        url = f"{self.base_url}/trending"
        if language:
            url += f"/{language}"
        url += f"?since={since}"
        
        response = self._make_request(url)
        
        if not response:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        repositories = []
        
        repo_items = soup.find_all('article', class_='Box-row')
        for item in repo_items:
            repo_link = item.find('h2').find('a')
            if not repo_link:
                continue
            
            repo_url = urljoin(self.base_url, repo_link['href'])
            repo_full_name = repo_link['href'].strip('/')
            username, repo_name = repo_full_name.split('/')
            
            # Description
            desc_elem = item.find('p', class_='col-9')
            description = desc_elem.text.strip() if desc_elem else None
            
            # Language
            lang_elem = item.find('span', {'itemprop': 'programmingLanguage'})
            language = lang_elem.text.strip() if lang_elem else None
            
            # Stars today
            stars_today = 0
            stars_elem = item.find('span', class_='d-inline-block')
            if stars_elem and 'stars today' in stars_elem.text:
                stars_today = self._parse_number(stars_elem.text.split()[0])
            
            repositories.append({
                'name': repo_name,
                'full_name': repo_full_name,
                'description': description,
                'url': repo_url,
                'language': language,
                'stars_today': stars_today,
                'owner': username
            })
        
        return repositories
