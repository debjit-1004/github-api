import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models.github_models import APIResponse, GitHubUser
from services.github_scraper import GitHubScraper

router = APIRouter(prefix="/api/users", tags=["Users"])
scraper = GitHubScraper()

@router.get("/{username}", response_model=APIResponse)
async def get_user_profile(username: str):
    """
    Get GitHub user profile information
    
    - **username**: GitHub username
    """
    try:
        user_data = scraper.get_user_profile(username)
        
        if "error" in user_data:
            raise HTTPException(status_code=404, detail=user_data["error"])
        
        return APIResponse(
            success=True,
            data=user_data,
            message=f"Successfully fetched profile for {username}"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch user profile"
        )

@router.get("/{username}/repos", response_model=APIResponse)
async def get_user_repositories(
    username: str,
    page: int = Query(1, ge=1, description="Page number")
):
    """
    Get user's public repositories
    
    - **username**: GitHub username
    - **page**: Page number for pagination
    """
    try:
        repos = scraper.get_user_repositories(username, page)
        
        return APIResponse(
            success=True,
            data=repos,
            message=f"Successfully fetched repositories for {username}"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch user repositories"
        )

@router.get("/{username}/followers", response_model=APIResponse)
async def get_user_followers(username: str):
    """
    Get user's followers (basic scraping)
    
    - **username**: GitHub username
    """
    try:
        # This would require more complex scraping or API access
        # For now, return placeholder
        return APIResponse(
            success=True,
            data={"message": "Followers endpoint - requires enhanced scraping"},
            message="Followers data requires GitHub API token for full functionality"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch followers"
        )

@router.get("/{username}/following", response_model=APIResponse)
async def get_user_following(username: str):
    """
    Get users that this user is following
    
    - **username**: GitHub username
    """
    try:
        # This would require more complex scraping or API access
        return APIResponse(
            success=True,
            data={"message": "Following endpoint - requires enhanced scraping"},
            message="Following data requires GitHub API token for full functionality"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch following"
        )

@router.get("/{username}/gists", response_model=APIResponse)
async def get_user_gists(username: str):
    """
    Get user's public gists
    
    - **username**: GitHub username
    """
    try:
        # Placeholder for gists scraping
        return APIResponse(
            success=True,
            data={"message": "Gists endpoint - requires enhanced scraping"},
            message="Gists data requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch gists"
        )

@router.get("/{username}/events", response_model=APIResponse)
async def get_user_events(username: str):
    """
    Get user's public events/activity
    
    - **username**: GitHub username
    """
    try:
        # Placeholder for events scraping
        return APIResponse(
            success=True,
            data={"message": "Events endpoint - requires enhanced scraping"},
            message="Events data requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch events"
        )
