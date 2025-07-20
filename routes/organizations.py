from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models.github_models import APIResponse
from services.github_scraper import GitHubScraper

router = APIRouter(prefix="/api/organizations", tags=["Organizations"])
scraper = GitHubScraper()

@router.get("/{org_name}", response_model=APIResponse)
async def get_organization_info(org_name: str):
    """
    Get GitHub organization information
    
    - **org_name**: Organization name
    """
    try:
        org_data = scraper.get_organization_info(org_name)
        
        if "error" in org_data:
            raise HTTPException(status_code=404, detail=org_data["error"])
        
        return APIResponse(
            success=True,
            data=org_data,
            message=f"Successfully fetched organization {org_name}"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch organization information"
        )

@router.get("/{org_name}/repos", response_model=APIResponse)
async def get_organization_repositories(
    org_name: str,
    page: int = Query(1, ge=1, description="Page number")
):
    """
    Get organization repositories
    
    - **org_name**: Organization name
    - **page**: Page number for pagination
    """
    try:
        repos = scraper.get_user_repositories(org_name, page)  # Same method works for orgs
        
        return APIResponse(
            success=True,
            data=repos,
            message=f"Successfully fetched repositories for {org_name}"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch organization repositories"
        )

@router.get("/{org_name}/members", response_model=APIResponse)
async def get_organization_members(org_name: str):
    """
    Get organization public members
    
    - **org_name**: Organization name
    """
    try:
        # Placeholder for members scraping - requires more complex implementation
        return APIResponse(
            success=True,
            data={"message": "Organization members endpoint - requires enhanced scraping"},
            message="Organization members requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch organization members"
        )

@router.get("/{org_name}/events", response_model=APIResponse)
async def get_organization_events(org_name: str):
    """
    Get organization public events
    
    - **org_name**: Organization name
    """
    try:
        # Placeholder for events scraping
        return APIResponse(
            success=True,
            data={"message": "Organization events endpoint - requires enhanced scraping"},
            message="Organization events requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch organization events"
        )
