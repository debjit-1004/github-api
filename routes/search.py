from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models.github_models import APIResponse
from services.github_scraper import GitHubScraper

router = APIRouter(prefix="/api/search", tags=["Search"])
scraper = GitHubScraper()

@router.get("/repositories", response_model=APIResponse)
async def search_repositories(
    q: str = Query(..., description="Search query"),
    sort: str = Query("stars", regex="^(stars|forks|updated)$", description="Sort by"),
    order: str = Query("desc", regex="^(asc|desc)$", description="Sort order")
):
    """
    Search GitHub repositories
    
    - **q**: Search query
    - **sort**: Sort by (stars, forks, updated)
    - **order**: Sort order (asc, desc)
    """
    try:
        repositories = scraper.search_repositories(q, sort, order)
        
        return APIResponse(
            success=True,
            data=repositories,
            message=f"Found {len(repositories)} repositories"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to search repositories"
        )

@router.get("/users", response_model=APIResponse)
async def search_users(
    q: str = Query(..., description="Search query for users")
):
    """
    Search GitHub users
    
    - **q**: Search query for users
    """
    try:
        # Placeholder for user search - requires more complex scraping
        return APIResponse(
            success=True,
            data={"message": "User search endpoint - requires enhanced scraping"},
            message="User search requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to search users"
        )

@router.get("/code", response_model=APIResponse)
async def search_code(
    q: str = Query(..., description="Search query for code")
):
    """
    Search code in GitHub repositories
    
    - **q**: Search query for code
    """
    try:
        # Placeholder for code search - requires GitHub API or advanced scraping
        return APIResponse(
            success=True,
            data={"message": "Code search endpoint - requires GitHub API access"},
            message="Code search requires GitHub API token for functionality"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to search code"
        )

@router.get("/issues", response_model=APIResponse)
async def search_issues(
    q: str = Query(..., description="Search query for issues")
):
    """
    Search issues across GitHub
    
    - **q**: Search query for issues
    """
    try:
        # Placeholder for issue search - requires GitHub API or advanced scraping
        return APIResponse(
            success=True,
            data={"message": "Issue search endpoint - requires enhanced scraping"},
            message="Issue search requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to search issues"
        )

@router.get("/topics", response_model=APIResponse)
async def search_topics(
    q: str = Query(..., description="Search query for topics")
):
    """
    Search GitHub topics
    
    - **q**: Search query for topics
    """
    try:
        # Placeholder for topic search
        return APIResponse(
            success=True,
            data={"message": "Topic search endpoint - requires enhanced scraping"},
            message="Topic search requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to search topics"
        )
