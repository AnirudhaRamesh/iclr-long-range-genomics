#!/bin/bash

# This script helps set up the GitHub repository for hosting this website on GitHub Pages

echo "=========================================================="
echo "   Setting up Git repository for GitHub Pages"
echo "=========================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git repository if it doesn't exist
if [ ! -d ".git" ]; then
    git init
    echo "✓ Git repository initialized."
else
    echo "✓ Git repository already exists."
fi

# Check for .gitignore
if [ -f ".gitignore" ]; then
    echo "✓ .gitignore file found."
else
    echo "Warning: .gitignore file not found. This might result in unnecessary files being committed."
fi

# Add all files to git
git add .
echo "✓ Files added to git staging area."

# Set up user information if not already set
if [ -z "$(git config user.name)" ]; then
    echo ""
    echo "Git user name not found. Please set it now."
    read -p "Enter your name: " git_name
    git config user.name "$git_name"
fi

if [ -z "$(git config user.email)" ]; then
    echo ""
    echo "Git user email not found. Please set it now."
    read -p "Enter your email: " git_email
    git config user.email "$git_email"
fi

# Commit changes
git commit -m "Initial website commit"
echo "✓ Changes committed."

# Instructions for connecting to GitHub
echo ""
echo "=========================================================="
echo "   Next steps to publish your website on GitHub Pages"
echo "=========================================================="
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Name your repository (e.g., 'ssm-genomics-website')"
echo "   - Choose public visibility (required for GitHub Pages)"
echo "   - Do NOT initialize the repository with a README or .gitignore"
echo "   - Click 'Create repository'"
echo ""
echo "2. Connect this local repository to your GitHub repository:"
echo "   git remote add origin https://github.com/yourusername/your-repo-name.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Enable GitHub Pages:"
echo "   - Go to your repository on GitHub"
echo "   - Navigate to Settings > Pages"
echo "   - Under 'Source', select 'main' branch"
echo "   - Click Save"
echo ""
echo "Your website will be available at: https://yourusername.github.io/your-repo-name/"
echo ""
echo "4. Using a custom domain (optional):"
echo "   - Uncomment and update the CNAME file with your domain"
echo "   - In GitHub repository settings > Pages > Custom domain, add your domain"
echo "   - Set up the DNS records at your domain provider"
echo ""
echo "==========================================================" 