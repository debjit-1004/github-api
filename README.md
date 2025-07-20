# 🚀 GitHub API Scraper

A comprehensive GitHub API service built with **FastAPI** and **Beautiful Soup** for web scraping. This service provides extensive GitHub data access through RESTful APIs with advanced scraping capabilities.

## 🌟 Features

- **User Profiles**: Get detailed GitHub user information
- **Repository Data**: Access repository details, README content, languages, commits, and issues
- **Search Functionality**: Search repositories across GitHub
- **Trending Data**: Access trending repositories by language and time period
- **Organization Info**: Get organization details and repositories
- **Web Scraping**: Advanced scraping with Beautiful Soup for comprehensive data extraction
- **CORS Enabled**: Ready for frontend integration
- **Interactive Documentation**: Swagger UI and ReDoc documentation
- **Error Handling**: Comprehensive error handling and status codes

## 🛠 Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Beautiful Soup**: Web scraping library for parsing HTML
- **Requests**: HTTP library for making web requests
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application
- **Python 3.12+**: Modern Python with type hints

## 📋 API Endpoints

### 👤 Users
- `GET /api/users/{username}` - Get user profile information
- `GET /api/users/{username}/repos` - Get user repositories with README content
- `GET /api/users/{username}/followers` - Get user followers (placeholder)
- `GET /api/users/{username}/following` - Get users being followed (placeholder)
- `GET /api/users/{username}/gists` - Get user gists (placeholder)
- `GET /api/users/{username}/events` - Get user public events (placeholder)

### 📁 Repositories
- `GET /api/repos/{username}/{repo_name}` - Get detailed repository information
- `GET /api/repos/{username}/{repo_name}/readme` - Get repository README content
- `GET /api/repos/{username}/{repo_name}/languages` - Get repository programming languages
- `GET /api/repos/{username}/{repo_name}/commits` - Get repository commits
- `GET /api/repos/{username}/{repo_name}/issues` - Get repository issues
- `GET /api/repos/{username}/{repo_name}/contributors` - Get repository contributors (placeholder)
- `GET /api/repos/{username}/{repo_name}/releases` - Get repository releases (placeholder)
- `GET /api/repos/{username}/{repo_name}/branches` - Get repository branches (placeholder)
- `GET /api/repos/{username}/{repo_name}/pulls` - Get repository pull requests (placeholder)

### 🔍 Search
- `GET /api/search/repositories` - Search GitHub repositories
- `GET /api/search/users` - Search GitHub users (placeholder)
- `GET /api/search/code` - Search code in repositories (placeholder)
- `GET /api/search/issues` - Search issues across GitHub (placeholder)
- `GET /api/search/topics` - Search GitHub topics (placeholder)

### 📈 Trending
- `GET /api/trending/repositories` - Get trending repositories
- `GET /api/trending/developers` - Get trending developers (placeholder)
- `GET /api/trending/languages` - Get trending programming languages (placeholder)

### 🏢 Organizations
- `GET /api/organizations/{org_name}` - Get organization information
- `GET /api/organizations/{org_name}/repos` - Get organization repositories
- `GET /api/organizations/{org_name}/members` - Get organization members (placeholder)
- `GET /api/organizations/{org_name}/events` - Get organization events (placeholder)

### 🔧 Utility
- `GET /` - Interactive homepage with API documentation
- `GET /health` - Health check endpoint
- `GET /api/status` - API status and information
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- uv package manager (recommended) or pip

### Installation with uv (Recommended)

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd github-api
   ```

2. **Install uv (if not already installed):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create and activate virtual environment:**
   ```bash
   uv venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

### Installation with pip

1. **Clone and navigate:**
   ```bash
   git clone <your-repo-url>
   cd github-api
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

## 📖 Usage Examples

### Get User Profile
```bash
curl "http://localhost:8000/api/users/octocat"
```

### Get User Repositories
```bash
curl "http://localhost:8000/api/users/octocat/repos"
```

### Get Repository Information
```bash
curl "http://localhost:8000/api/repos/octocat/Hello-World"
```

### Get Repository README
```bash
curl "http://localhost:8000/api/repos/octocat/Hello-World/readme"
```

### Search Repositories
```bash
curl "http://localhost:8000/api/search/repositories?q=python%20machine%20learning&sort=stars&order=desc"
```

### Get Trending Repositories
```bash
curl "http://localhost:8000/api/trending/repositories?language=python&since=weekly"
```

## 🔧 Configuration

### Environment Variables
- `PORT`: Server port (default: 8000)
- Add other environment variables as needed

### CORS Configuration
The application is configured with CORS to allow requests from:
- `http://localhost:3000` (React development)
- `http://localhost:8000` (Local testing)
- Your production domain

## 🚀 Deployment on Render

### Step 1: Prepare for Deployment

1. **Ensure all files are in place:**
   - `main.py` - Main application file
   - `requirements.txt` - Dependencies
   - `render.yaml` - Render configuration (optional)

2. **Test locally:**
   ```bash
   python main.py
   ```

### Step 2: Create Render Service

1. **Sign up/Login to [Render](https://render.com)**

2. **Connect your GitHub repository:**
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub account
   - Select your repository

3. **Configure the service:**
   - **Name**: `github-api-scraper`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Instance Type**: Free tier or paid tier

### Step 3: Environment Variables (Optional)
Add any environment variables in the Render dashboard:
- `PORT`: Will be automatically set by Render
- Add others as needed

### Step 4: Deploy
1. Click "Create Web Service"
2. Render will automatically deploy your application
3. Your API will be available at `https://your-service-name.onrender.com`

### Alternative: Manual Deployment

Create a `render.yaml` file in your repository root:

```yaml
services:
  - type: web
    name: github-api-scraper
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: PORT
        value: 10000
```

## 📱 Frontend Integration

### JavaScript/React Example
```javascript
// Get user profile
const response = await fetch('https://your-api.onrender.com/api/users/octocat');
const userData = await response.json();

// Get repositories
const reposResponse = await fetch('https://your-api.onrender.com/api/users/octocat/repos');
const repositories = await reposResponse.json();
```

### Python Example
```python
import requests

# Get user profile
response = requests.get('https://your-api.onrender.com/api/users/octocat')
user_data = response.json()

# Get repositories
repos_response = requests.get('https://your-api.onrender.com/api/users/octocat/repos')
repositories = repos_response.json()
```

## 🔍 API Response Format

All endpoints return a consistent response format:

```json
{
  "success": true,
  "data": {
    // Actual data here
  },
  "message": "Success message",
  "error": null
}
```

Error responses:
```json
{
  "success": false,
  "data": null,
  "message": "Error description",
  "error": "Detailed error message"
}
```

## ⚠️ Rate Limiting & Best Practices

### Web Scraping Guidelines
- The service implements respectful scraping with delays
- Rate limiting is handled through request throttling
- User-Agent headers are set to identify the scraper

### Best Practices
1. **Cache responses** when possible to reduce API calls
2. **Handle errors** gracefully in your frontend
3. **Respect GitHub's terms of service** when using scraped data
4. **Monitor usage** to avoid overwhelming the service

## 🔧 Development

### Project Structure
```
github-api/
├── main.py                 # Main application file
├── requirements.txt        # Dependencies
├── models/
│   ├── __init__.py
│   └── github_models.py    # Pydantic models
├── routes/
│   ├── __init__.py
│   ├── users.py           # User endpoints
│   ├── repositories.py    # Repository endpoints
│   ├── search.py          # Search endpoints
│   ├── trending.py        # Trending endpoints
│   └── organizations.py   # Organization endpoints
└── services/
    ├── __init__.py
    └── github_scraper.py   # Web scraping service
```

### Adding New Endpoints
1. Create new route in appropriate router file
2. Add scraping logic to `GitHubScraper` class
3. Define response models in `github_models.py`
4. Update documentation

### Testing
```bash
# Install development dependencies
uv pip install pytest httpx

# Run tests (create test files as needed)
pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🐛 Issues & Support

- **Bug Reports**: Open an issue on GitHub
- **Feature Requests**: Open an issue with the "enhancement" label
- **Questions**: Check the documentation or open a discussion

## 🙏 Acknowledgments

- **FastAPI** - For the excellent web framework
- **Beautiful Soup** - For powerful web scraping capabilities
- **GitHub** - For providing the data source
- **Render** - For easy deployment platform

---

Built with ❤️ using FastAPI and Beautiful Soup

A FastAPI-based backend for fetching and summarizing GitHub repository profiles.

## Features

- Fetches GitHub repository profile data via a simple API.
- CORS enabled for frontend integration (e.g., React on `localhost:3000`).
- Easy to extend with additional routes.

## Requirements

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/github-scrapper.git
   cd github-scrapper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload --port 8000
```

- The API will be available at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### `GET /api/readme`

Fetch GitHub repository profile data.

**Query Parameters:**
- `repo` (string, required): The repository in the format `owner/repo_name` (e.g., `torvalds/linux`).

**Example Request:**
```
GET http://localhost:3000/api/readme?repo=https://github.com/K-is-SAD
```

**Example Response:**
```json
{
  "name": "linux",
  "bio": "Linux kernel source tree",
  "repositories":[
    {"repo":, "readme":},
    {},
    {},
    
  ]
  ...
}
```

### `GET /`

Health check endpoint.

**Response:**
```json
{ "message": "Hello World" }
```

## Frontend Integration

If you have a frontend running on `localhost:3000`, you can fetch data like this:

```js
fetch("http://localhost:3000/api/readme?repo=https://github.com/K-is-SAD")
  .then(res => res.json())
  .then(data => console.log(data));
```

## License

MIT