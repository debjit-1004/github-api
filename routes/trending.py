from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models.github_models import APIResponse
from services.github_scraper import GitHubScraper

router = APIRouter(prefix="/api/trending", tags=["Trending"])
scraper = GitHubScraper()

@router.get("/repositories", response_model=APIResponse)
async def get_trending_repositories(
    language: str = Query("", description="Programming language filter"),
    since: str = Query("daily", regex="^(daily|weekly|monthly)$", description="Time period")
):
    """
    Get trending GitHub repositories
    
    - **language**: Programming language filter (optional)
    - **since**: Time period (daily, weekly, monthly)
    """
    try:
        repositories = scraper.get_trending_repositories(language, since)
        
        return APIResponse(
            success=True,
            data=repositories,
            message=f"Found {len(repositories)} trending repositories"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch trending repositories"
        )

@router.get("/developers", response_model=APIResponse)
async def get_trending_developers(
    language: str = Query("", description="Programming language filter"),
    since: str = Query("daily", regex="^(daily|weekly|monthly)$", description="Time period")
):
    """
    Get trending GitHub developers
    
    - **language**: Programming language filter (optional)
    - **since**: Time period (daily, weekly, monthly)
    """
    try:
        # Placeholder for trending developers - requires more complex scraping
        return APIResponse(
            success=True,
            data={"message": "Trending developers endpoint - requires enhanced scraping"},
            message="Trending developers requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch trending developers"
        )

@router.get("/languages", response_model=APIResponse)
async def get_trending_languages():
    """
    Get trending programming languages
    """
    try:
        # Placeholder for trending languages
        return APIResponse(
            success=True,
            data={"message": "Trending languages endpoint - requires enhanced scraping"},
            message="Trending languages requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch trending languages"
        )
