#!/bin/bash

# Check if a repository URL was provided
if [ -z "$1" ]; then
  echo "Please provide a GitHub repository URL"
  echo "Usage: ./setup_github.sh \"https://github.com/username/repository.git\""
  exit 1
fi

# Add the remote repository
git remote add origin $1

# Push to the main branch
git push -u origin main

echo "GitHub repository setup complete!"
echo "Your site will be available at:"
echo "https://$(echo $1 | sed -E 's/.*github\.com\/([^\/]+)\/.*/\1/').github.io/$(echo $1 | sed -E 's/.*github\.com\/[^\/]+\/([^\.]+).*/\1/')/" 