#!/bin/bash

# Check if a commit message was provided
if [ -z "$1" ]; then
  echo "Please provide a commit message"
  echo "Usage: ./deploy.sh \"Your commit message\""
  exit 1
fi

# Add all files to git
git add .

# Commit with the provided message
git commit -m "$1"

# Push to the main branch
git push origin main

echo "Deployment initiated! Your site will be available at:"
echo "https://<your-github-username>.github.io/<repository-name>/"
echo "Please replace <your-github-username> and <repository-name> with your actual GitHub username and repository name." 