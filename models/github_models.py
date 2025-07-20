from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class GitHubUser(BaseModel):
    username: str
    name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    blog: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    followers: Optional[int] = None
    following: Optional[int] = None
    public_repos: Optional[int] = None
    public_gists: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class GitHubRepository(BaseModel):
    name: str
    full_name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    clone_url: Optional[str] = None
    ssh_url: Optional[str] = None
    homepage: Optional[str] = None
    language: Optional[str] = None
    languages: Optional[Dict[str, int]] = None
    size: Optional[int] = None
    stargazers_count: Optional[int] = None
    watchers_count: Optional[int] = None
    forks_count: Optional[int] = None
    open_issues_count: Optional[int] = None
    default_branch: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    pushed_at: Optional[str] = None
    is_private: Optional[bool] = None
    is_fork: Optional[bool] = None
    is_archived: Optional[bool] = None
    topics: Optional[List[str]] = None
    readme_content: Optional[str] = None

class GitHubCommit(BaseModel):
    sha: str
    message: str
    author: Optional[str] = None
    date: Optional[str] = None
    url: Optional[str] = None
    additions: Optional[int] = None
    deletions: Optional[int] = None
    files_changed: Optional[int] = None

class GitHubIssue(BaseModel):
    number: int
    title: str
    body: Optional[str] = None
    state: str
    author: Optional[str] = None
    assignees: Optional[List[str]] = None
    labels: Optional[List[str]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    closed_at: Optional[str] = None
    url: Optional[str] = None

class GitHubPullRequest(BaseModel):
    number: int
    title: str
    body: Optional[str] = None
    state: str
    author: Optional[str] = None
    base: Optional[str] = None
    head: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    merged_at: Optional[str] = None
    url: Optional[str] = None
    additions: Optional[int] = None
    deletions: Optional[int] = None
    changed_files: Optional[int] = None

class GitHubRelease(BaseModel):
    tag_name: str
    name: Optional[str] = None
    body: Optional[str] = None
    draft: bool = False
    prerelease: bool = False
    created_at: Optional[str] = None
    published_at: Optional[str] = None
    author: Optional[str] = None
    url: Optional[str] = None
    download_count: Optional[int] = None

class GitHubBranch(BaseModel):
    name: str
    commit_sha: Optional[str] = None
    protected: Optional[bool] = None

class GitHubContributor(BaseModel):
    username: str
    avatar_url: Optional[str] = None
    contributions: Optional[int] = None
    url: Optional[str] = None

class GitHubOrganization(BaseModel):
    name: str
    display_name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    blog: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    public_repos: Optional[int] = None
    public_members: Optional[int] = None
    created_at: Optional[str] = None

class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
