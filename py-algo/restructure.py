#!/usr/bin/env python3
"""
Script to restructure the py-algo directory into one problem per file.
Extracts methods from Solution classes and creates individual files.
"""

import os
import re
import ast
from pathlib import Path

# Configuration
BASE_DIR = Path("/Users/koonerts/.proj/algo/py-algo")
OUTPUT_DIR = BASE_DIR / "reorganized"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Create an __init__.py file in the output directory
with open(OUTPUT_DIR / "__init__.py", "w") as f:
    f.write("# This file marks the directory as a Python package\n")

# Create a README.md file in the output directory
with open(OUTPUT_DIR / "README.md", "w") as f:
    f.write("""# Python Algorithm Problems

This directory contains algorithm problems organized by category, with one problem per file.

## Structure

Each problem is in its own file with:
- Descriptive docstring explaining the problem
- Implementation of the solution
- Example usage with test cases

## Categories

""")

# Category mappings
CATEGORIES = {
    "arrays-and-strings.py": "arrays",
    "binary-trees.py": "trees",
    "trees-and-graphs.py": "trees",
    "linked-list.py": "linked_lists",
    "dynamic-programming.py": "dp",
    "math-and-bitwise-operations.py": "math",
    "custom-data-structures.py": "data_structures",
    "sort-and-search.py": "sorting",
    "stacks.py": "stacks_queues",
    "queues.py": "stacks_queues",
    "divide-and-conquer.py": "divide_conquer",
    "recursion.py": "recursion",
}

# Files to process
DIRS_TO_PROCESS = ["leetcode", "algo-expert", "grokk-tci"]


# Utility function to convert method name to snake_case
def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def extract_docstring(func_node):
    """Extract docstring from AST function node"""
    if (
        isinstance(func_node, ast.FunctionDef)
        and func_node.body
        and isinstance(func_node.body[0], ast.Expr)
        and isinstance(func_node.body[0].value, ast.Constant)
        and isinstance(func_node.body[0].value.value, str)
    ):
        return func_node.body[0].value.value
    return ""


def process_file(file_path, category_problems=None):
    """Process a single file to extract problems"""
    print(f"Processing {file_path}...")

    with open(file_path, "r") as f:
        content = f.read()

    # Parse the file
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        return

    # Determine category from filename
    filename = os.path.basename(file_path)
    category = CATEGORIES.get(filename, "misc")

    # Create category directory
    category_dir = OUTPUT_DIR / category
    os.makedirs(category_dir, exist_ok=True)

    # Extract all functions
    extracted_functions = []

    # Get standalone functions
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            extracted_functions.append(extract_function(node, content))

    # Get methods from Solution class
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            for method in node.body:
                if isinstance(method, ast.FunctionDef) and not method.name.startswith(
                    "_"
                ):
                    # Convert method to standalone function
                    extracted_functions.append(extract_method(method, content))

    # Track the problems processed
    processed_problems = []

    # Write each function to its own file
    for func_name, func_code, docstring in extracted_functions:
        if func_name in ("__init__", "print_matrix"):
            continue

        # Convert function name to snake_case for filename
        file_name = f"{camel_to_snake(func_name)}.py"
        output_path = category_dir / file_name

        # Prepare function content with doc and example
        problem_title = " ".join(re.findall("[A-Z][^A-Z]*", func_name))
        if not problem_title:
            problem_title = func_name.capitalize()

        with open(output_path, "w") as f:
            f.write(f'"""\n{problem_title}\n\n')
            if docstring:
                f.write(f"{docstring.strip()}\n")
            f.write('"""\n\n\n')

            # Add imports if needed (basic ones)
            if "collections" in func_code:
                f.write("import collections\n")
            if "heapq" in func_code:
                f.write("from heapq import *\n")
            if "defaultdict" in func_code:
                f.write("from collections import defaultdict\n")
            if "Counter" in func_code:
                f.write("from collections import Counter\n")
            if "deque" in func_code:
                f.write("from collections import deque\n")
            if any(x in func_code for x in ["math.", "sqrt", "ceil", "floor"]):
                f.write("import math\n")
            if "string." in func_code:
                f.write("import string\n")

            f.write("\n")

            # Write the function definition
            f.write(func_code)

            # Add example usage
            f.write("\n\n# Example usage\n")
            f.write('if __name__ == "__main__":\n')
            f.write(f"    # TODO: Add example calls to {func_name}\n")
            f.write(f"    print({func_name}([]))\n")

        print(f"Created {output_path}")

        # Track this problem for README updates
        processed_problems.append((problem_title, file_name))

        # If we're tracking category problems, add this one
        if category_problems is not None and category in category_problems:
            category_problems[category].extend(processed_problems)

    return processed_problems


def extract_function(func_node, source):
    """Extract standalone function from AST node"""
    func_name = func_node.name

    # Get line numbers
    start_line = func_node.lineno
    end_line = 0
    for node in ast.walk(func_node):
        if hasattr(node, "lineno"):
            end_line = max(end_line, node.lineno)

    # Additional lines for function end (estimate)
    end_line += 10
    end_line = min(end_line, len(source.splitlines()))

    # Extract function source code
    lines = source.splitlines()[start_line - 1 : end_line]
    func_source = []
    indent = 0
    for i, line in enumerate(lines):
        if i == 0:
            indent = len(line) - len(line.lstrip())
            func_source.append(line)
        else:
            # Check if this line belongs to the function
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= indent and i > 1 and line.strip():
                break
            func_source.append(line)

    func_code = "\n".join(func_source)
    docstring = extract_docstring(func_node)

    return func_name, func_code, docstring


def extract_method(method_node, source):
    """Extract method from a class and convert to standalone function"""
    method_name = method_node.name

    # Get line numbers
    start_line = method_node.lineno
    end_line = 0
    for node in ast.walk(method_node):
        if hasattr(node, "lineno"):
            end_line = max(end_line, node.lineno)

    # Additional lines for method end (estimate)
    end_line += 10
    end_line = min(end_line, len(source.splitlines()))

    # Extract method source code
    lines = source.splitlines()[start_line - 1 : end_line]
    method_source = []
    indent = 0
    for i, line in enumerate(lines):
        if i == 0:
            # Method definition
            indent = len(line) - len(line.lstrip())
            # Convert "def method(self, ..." to "def method(..."
            line = re.sub(r"def\s+(\w+)\s*\(\s*self\s*,?\s*", r"def \1(", line)
            method_source.append(line)
        else:
            # Check if this line belongs to the method
            if line.strip():
                current_indent = len(line) - len(line.lstrip())
                if current_indent <= indent and i > 1:
                    break
            method_source.append(line)

    func_code = "\n".join(method_source)
    docstring = extract_docstring(method_node)

    return method_name, func_code, docstring


def create_category_structure():
    """Create directory structure for all categories with README and __init__.py files"""
    # Create directories for all categories defined in mapping
    categories = set(CATEGORIES.values())
    category_count = {}

    for category in categories:
        category_dir = OUTPUT_DIR / category
        os.makedirs(category_dir, exist_ok=True)

        # Add __init__.py file
        with open(category_dir / "__init__.py", "w") as f:
            f.write(f"# This file marks the {category} directory as a Python package\n")

        # Create README.md template
        with open(category_dir / "README.md", "w") as f:
            title = category.replace("_", " ").title()
            f.write(f"""# {title} Algorithms

This directory contains algorithm problems related to {title.lower()}.

## Problems

""")

        category_count[category] = 0

    return category_count


def update_readme(category_count):
    """Update main README.md with category information"""
    # Update main README with category list
    with open(OUTPUT_DIR / "README.md", "a") as f:
        for category, count in sorted(category_count.items()):
            title = category.replace("_", " ").title()
            f.write(f"- [{title}](./{category}/) - {count} problems\n")


def update_category_readme(category, problems):
    """Update category README with problem list"""
    if not problems:
        return

    category_dir = OUTPUT_DIR / category
    readme_path = category_dir / "README.md"

    with open(readme_path, "a") as f:
        for problem_name, file_name in sorted(problems):
            f.write(f"- [{problem_name}](./{file_name})\n")


def main():
    """Main function to process all files"""
    # Create directory structure first
    category_count = create_category_structure()
    category_problems = {category: [] for category in category_count.keys()}

    for dir_name in DIRS_TO_PROCESS:
        dir_path = BASE_DIR / dir_name
        if not dir_path.exists():
            print(f"Directory {dir_path} does not exist, skipping.")
            continue

        # Process Python files in the directory
        for file_path in dir_path.glob("*.py"):
            if file_path.name in ("__init__.py", "__pycache__"):
                continue

            # Process file and track problems
            problems = process_file(file_path, category_problems)

            # Update category count if problems were found
            if problems:
                filename = os.path.basename(file_path)
                category = CATEGORIES.get(filename, "misc")
                if category in category_count:
                    category_count[category] += len(problems)

        # Process files in subdirectories
        for subdir in dir_path.glob("**/"):
            if subdir == dir_path:
                continue
            for file_path in subdir.glob("*.py"):
                if file_path.name in ("__init__.py", "__pycache__"):
                    continue

                # Process file and track problems
                problems = process_file(file_path, category_problems)

                # Update category count if problems were found
                if problems:
                    filename = os.path.basename(file_path)
                    category = CATEGORIES.get(filename, "misc")
                    if category in category_count:
                        category_count[category] += len(problems)

    # Update the category count in the main README
    update_readme(category_count)

    # Update category READMEs with problem lists
    for category, problems in category_problems.items():
        update_category_readme(category, problems)

    print("\nRestructuring complete!")


if __name__ == "__main__":
    main()
