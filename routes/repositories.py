from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from models.github_models import APIResponse, GitHubRepository
from services.github_scraper import GitHubScraper

router = APIRouter(prefix="/api/repos", tags=["Repositories"])
scraper = GitHubScraper()

@router.get("/{username}/{repo_name}", response_model=APIResponse)
async def get_repository_info(username: str, repo_name: str):
    """
    Get detailed repository information
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    """
    try:
        repo_data = scraper.get_repository_info(username, repo_name)
        
        if "error" in repo_data:
            raise HTTPException(status_code=404, detail=repo_data["error"])
        
        return APIResponse(
            success=True,
            data=repo_data,
            message=f"Successfully fetched repository {username}/{repo_name}"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch repository information"
        )

@router.get("/{username}/{repo_name}/readme", response_model=APIResponse)
async def get_repository_readme(username: str, repo_name: str):
    """
    Get repository README content
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    """
    try:
        readme_content = scraper.get_repository_readme(username, repo_name)
        
        if not readme_content:
            raise HTTPException(status_code=404, detail="README not found")
        
        return APIResponse(
            success=True,
            data={"readme": readme_content},
            message="Successfully fetched README"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch README"
        )

@router.get("/{username}/{repo_name}/languages", response_model=APIResponse)
async def get_repository_languages(username: str, repo_name: str):
    """
    Get repository programming languages
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    """
    try:
        languages = scraper.get_repository_languages(username, repo_name)
        
        return APIResponse(
            success=True,
            data=languages,
            message="Successfully fetched repository languages"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch languages"
        )

@router.get("/{username}/{repo_name}/commits", response_model=APIResponse)
async def get_repository_commits(
    username: str, 
    repo_name: str,
    page: int = Query(1, ge=1, description="Page number")
):
    """
    Get repository commits
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    - **page**: Page number for pagination
    """
    try:
        commits = scraper.get_repository_commits(username, repo_name, page)
        
        return APIResponse(
            success=True,
            data=commits,
            message="Successfully fetched repository commits"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch commits"
        )

@router.get("/{username}/{repo_name}/issues", response_model=APIResponse)
async def get_repository_issues(
    username: str, 
    repo_name: str,
    state: str = Query("open", regex="^(open|closed|all)$", description="Issue state")
):
    """
    Get repository issues
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    - **state**: Issue state (open, closed, all)
    """
    try:
        issues = scraper.get_repository_issues(username, repo_name, state)
        
        return APIResponse(
            success=True,
            data=issues,
            message="Successfully fetched repository issues"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch issues"
        )

@router.get("/{username}/{repo_name}/contributors", response_model=APIResponse)
async def get_repository_contributors(username: str, repo_name: str):
    """
    Get repository contributors
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    """
    try:
        # Placeholder for contributors scraping
        return APIResponse(
            success=True,
            data={"message": "Contributors endpoint - requires enhanced scraping"},
            message="Contributors data requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch contributors"
        )

@router.get("/{username}/{repo_name}/releases", response_model=APIResponse)
async def get_repository_releases(username: str, repo_name: str):
    """
    Get repository releases
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    """
    try:
        # Placeholder for releases scraping
        return APIResponse(
            success=True,
            data={"message": "Releases endpoint - requires enhanced scraping"},
            message="Releases data requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch releases"
        )

@router.get("/{username}/{repo_name}/branches", response_model=APIResponse)
async def get_repository_branches(username: str, repo_name: str):
    """
    Get repository branches
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    """
    try:
        # Placeholder for branches scraping
        return APIResponse(
            success=True,
            data={"message": "Branches endpoint - requires enhanced scraping"},
            message="Branches data requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch branches"
        )

@router.get("/{username}/{repo_name}/pulls", response_model=APIResponse)
async def get_repository_pull_requests(
    username: str, 
    repo_name: str,
    state: str = Query("open", regex="^(open|closed|all)$", description="PR state")
):
    """
    Get repository pull requests
    
    - **username**: Repository owner's username
    - **repo_name**: Repository name
    - **state**: Pull request state (open, closed, all)
    """
    try:
        # Placeholder for pull requests scraping
        return APIResponse(
            success=True,
            data={"message": "Pull requests endpoint - requires enhanced scraping"},
            message="Pull requests data requires additional scraping implementation"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to fetch pull requests"
        )
