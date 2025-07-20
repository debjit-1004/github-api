from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import route modules
from routes import (
    users_router,
    repositories_router,
    search_router,
    trending_router,
    organizations_router
)
from models.github_models import APIResponse

# Create FastAPI app
app = FastAPI(
    title="GitHub API Scraper",
    description="A comprehensive GitHub API scraper with web scraping capabilities",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
allowed_origins_env = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000,*')
origins = [origin.strip() for origin in allowed_origins_env.split(',')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users_router)
app.include_router(repositories_router)
app.include_router(search_router)
app.include_router(trending_router)
app.include_router(organizations_router)

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint with API documentation"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitHub API Scraper</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #24292e; border-bottom: 3px solid #0366d6; padding-bottom: 10px; }
            h2 { color: #0366d6; margin-top: 30px; }
            .endpoint { background: #f6f8fa; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #0366d6; }
            .method { background: #28a745; color: white; padding: 4px 8px; border-radius: 3px; font-size: 12px; font-weight: bold; }
            .description { margin-top: 8px; color: #586069; }
            a { color: #0366d6; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .feature { background: #e1f5fe; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #0288d1; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 GitHub API Scraper</h1>
            <p>A comprehensive GitHub API service built with FastAPI and web scraping capabilities using Beautiful Soup.</p>
            
            <div class="feature">
                <strong>🔧 Interactive Documentation:</strong>
                <ul>
                    <li><a href="/docs" target="_blank">Swagger UI Documentation</a> - Test APIs interactively</li>
                    <li><a href="/redoc" target="_blank">ReDoc Documentation</a> - Beautiful API docs</li>
                </ul>
            </div>

            <h2>📋 Available API Endpoints</h2>
            
            <h3>👤 Users</h3>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/users/{username}</strong>
                <div class="description">Get GitHub user profile information</div>
            </div>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/users/{username}/repos</strong>
                <div class="description">Get user's public repositories with README content</div>
            </div>
            
            <h3>📁 Repositories</h3>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/repos/{username}/{repo_name}</strong>
                <div class="description">Get detailed repository information</div>
            </div>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/repos/{username}/{repo_name}/readme</strong>
                <div class="description">Get repository README content</div>
            </div>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/repos/{username}/{repo_name}/languages</strong>
                <div class="description">Get repository programming languages</div>
            </div>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/repos/{username}/{repo_name}/commits</strong>
                <div class="description">Get repository commits</div>
            </div>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/repos/{username}/{repo_name}/issues</strong>
                <div class="description">Get repository issues</div>
            </div>
            
            <h3>🔍 Search</h3>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/search/repositories</strong>
                <div class="description">Search GitHub repositories</div>
            </div>
            
            <h3>📈 Trending</h3>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/trending/repositories</strong>
                <div class="description">Get trending GitHub repositories</div>
            </div>
            
            <h3>🏢 Organizations</h3>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/organizations/{org_name}</strong>
                <div class="description">Get GitHub organization information</div>
            </div>
            <div class="endpoint">
                <span class="method">GET</span> <strong>/api/organizations/{org_name}/repos</strong>
                <div class="description">Get organization repositories</div>
            </div>

            <h2>🌟 Features</h2>
            <div class="feature">
                <strong>✅ Web Scraping:</strong> Advanced scraping with Beautiful Soup for comprehensive data extraction
            </div>
            <div class="feature">
                <strong>✅ README Content:</strong> Automatic README.md fetching from main/master branches
            </div>
            <div class="feature">
                <strong>✅ Language Detection:</strong> Programming language statistics for repositories
            </div>
            <div class="feature">
                <strong>✅ Trending Data:</strong> Access to GitHub trending repositories
            </div>
            <div class="feature">
                <strong>✅ CORS Enabled:</strong> Ready for frontend integration
            </div>
            <div class="feature">
                <strong>✅ Error Handling:</strong> Comprehensive error handling and status codes
            </div>

            <h2>🚀 Deploy to Render</h2>
            <p>This service is ready for deployment on <a href="https://render.com" target="_blank">Render</a>. See the README for deployment instructions.</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health", response_model=APIResponse)
async def health_check():
    """Health check endpoint"""
    return APIResponse(
        success=True,
        data={"status": "healthy", "version": "1.0.0"},
        message="GitHub API Scraper is running"
    )

@app.get("/api/status", response_model=APIResponse)
async def api_status():
    """API status endpoint"""
    return APIResponse(
        success=True,
        data={
            "api_version": "1.0.0",
            "endpoints_available": [
                "users", "repositories", "search", "trending", "organizations"
            ],
            "features": [
                "User profiles", "Repository details", "README scraping",
                "Language detection", "Trending repositories", "Organization info"
            ]
        },
        message="GitHub API Scraper is operational"
    )

# Legacy endpoint for backward compatibility
@app.get("/api/readme")
async def legacy_readme(repo: str):
    """Legacy endpoint - redirects to new user repos endpoint"""
    try:
        # Parse the old repo parameter format
        if "/" in repo:
            username = repo.split("/")[0].replace("https://github.com/", "")
            return JSONResponse(
                content={
                    "message": "This endpoint is deprecated. Please use /api/users/{username}/repos",
                    "new_endpoint": f"/api/users/{username}/repos"
                },
                status_code=301
            )
        else:
            username = repo.replace("https://github.com/", "")
            return JSONResponse(
                content={
                    "message": "This endpoint is deprecated. Please use /api/users/{username}/repos",
                    "new_endpoint": f"/api/users/{username}/repos"
                },
                status_code=301
            )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid repo parameter", "details": str(e)}
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
