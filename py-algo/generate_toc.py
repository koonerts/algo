#!/usr/bin/env python3
"""
Script to generate a table of contents for category README files.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("/Users/koonerts/.proj/algo/py-algo/reorganized")


def extract_problem_info(file_path):
    """Extract problem name and description from a Python file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract title from docstring
    title_match = re.search(r'"""[\s\n]*(.*?)[\s\n]*(?:\n|$)', content)
    title = title_match.group(1) if title_match else os.path.basename(file_path).replace('.py', '').replace('_', ' ').title()
    
    # Extract description
    desc_match = re.search(r'"""[\s\n]*.*?[\s\n]*(.*?)[\s\n]*"""', content, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""
    if description:
        # Take only the first sentence or line
        description = description.split('\n')[0].strip()
        if len(description) > 100:
            description = description[:97] + "..."
    
    return title, description


def update_category_readme(category):
    """Update category README with a table of contents"""
    category_dir = BASE_DIR / category
    readme_path = category_dir / "README.md"
    
    # Skip if directory doesn't exist
    if not category_dir.exists():
        return
    
    # Get all problem files
    problem_files = [f for f in os.listdir(category_dir) if f.endswith('.py') and f != '__init__.py']
    
    # Get problem info
    problems = []
    for file_name in problem_files:
        file_path = category_dir / file_name
        title, description = extract_problem_info(file_path)
        problems.append((title, file_name, description))
    
    # Sort problems alphabetically
    problems.sort(key=lambda x: x[0].lower())
    
    # Create new README content
    title = category.replace("_", " ").title()
    
    content = f"""# {title} Algorithms

This directory contains algorithm problems related to {title.lower()}.

## Table of Contents

| Problem | Description |
|---------|-------------|
"""
    
    for title, file_name, description in problems:
        content += f"| [{title}](./{file_name}) | {description} |\n"
    
    # Write the README
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Updated README for {category} with {len(problems)} problems")


def update_main_readme():
    """Update main README with category info and counts"""
    categories = [d for d in os.listdir(BASE_DIR) if os.path.isdir(BASE_DIR / d) and d not in ['.git', '__pycache__']]
    category_counts = {}
    
    for category in categories:
        problem_files = [f for f in os.listdir(BASE_DIR / category) if f.endswith('.py') and f != '__init__.py']
        category_counts[category] = len(problem_files)
    
    # Sort categories by count (descending)
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Create new README content
    content = """# Python Algorithm Problems

This directory contains algorithm problems organized by category, with one problem per file.

## Structure

Each problem is in its own file with:
- Descriptive docstring explaining the problem
- Implementation of the solution
- Example usage with test cases

## Categories

"""
    
    for category, count in sorted_categories:
        title = category.replace("_", " ").title()
        content += f"- [{title}](./{category}/) - {count} problems\n"
    
    # Write the README
    with open(BASE_DIR / "README.md", 'w') as f:
        f.write(content)
    
    print(f"Updated main README with {len(categories)} categories")


def main():
    """Generate table of contents for all category README files"""
    print("Generating table of contents for READMEs...")
    
    # Get all categories
    categories = [d for d in os.listdir(BASE_DIR) if os.path.isdir(BASE_DIR / d) and d not in ['.git', '__pycache__']]
    
    # Update each category README
    for category in categories:
        update_category_readme(category)
    
    # Update main README
    update_main_readme()
    
    print("Table of contents generation complete!")


if __name__ == "__main__":
    main()