#!/bin/bash

# Render the site
quarto render

# Copy rendered output to repo root
cp -r _site/* .

# Stage everything
git add .

# Commit with a timestamped message
git commit -m "Deploy site $(date '+%Y-%m-%d %H:%M:%S')"

# Push to GitHub
git push
