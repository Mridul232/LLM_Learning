<#
Simple PowerShell helper to create a GitHub repo and push the current folder.
Usage: Run this inside the to_upload folder in PowerShell.
Prerequisites:
- git installed and configured (user.name, user.email)
- Optionally `gh` (GitHub CLI) installed and authenticated for easier repo creation

This script will:
- initialize a git repo (if not already),
- add all files and commit,
- either create a GitHub repo via `gh` (if present) and push, or show the git remote add / push commands to run.
#>

param(
    [string]$RepoName = "",
    [switch]$Private
)

# Ensure we are in the script directory
Set-Location -Path $PSScriptRoot

if (-not $RepoName) {
    $RepoName = Read-Host "Enter the GitHub repo name to create (e.g. langchain-playground)"
}

# Initialize git if needed
if (-not (Test-Path .git)) {
    git init
}

git add .
git commit -m "Sanitized LangChain learning files: remove keys and exclude personal PDF" -q

# Use gh if available
$ghAvailable = $false
try { gh --version > $null 2>&1; $ghAvailable = $true } catch { $ghAvailable = $false }

if ($ghAvailable) {
    $visibility = 'public'
    if ($Private) { $visibility = 'private' }
    gh repo create Mridul232/$RepoName --$visibility --source=. --remote=origin --push
    Write-Host "Pushed to https://github.com/Mridul232/$RepoName"
} else {
    Write-Host "gh (GitHub CLI) not found. Run the following commands manually to push."
    Write-Host "Replace <URL> with your repository HTTPS URL (create the repo on github.com first)."
    Write-Host "git remote add origin https://github.com/Mridul232/$RepoName.git"
    Write-Host "git branch -M main"
    Write-Host "git push -u origin main"
}

Write-Host "Done. Remember to NOT commit your .env file which contains secrets."