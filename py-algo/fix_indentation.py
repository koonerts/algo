#!/usr/bin/env python3
"""
Script to fix indentation in the restructured Python files.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("/Users/koonerts/.proj/algo/py-algo/reorganized")


def fix_file(file_path):
    """Fix indentation in a Python file"""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Find function definitions that have improper indentation
    function_pattern = r'^\s+def\s+(\w+)\('
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        match = re.match(function_pattern, line)
        
        if match:
            # Found a function with indentation
            func_name = match.group(1)
            
            # Calculate the indentation to remove
            indent_to_remove = len(line) - len(line.lstrip())
            
            # Add the fixed function definition
            fixed_lines.append(f"def {func_name}{line.lstrip()[4 + len(func_name):]}")
            
            # Process the function body
            i += 1
            while i < len(lines):
                body_line = lines[i]
                # Check if we're still in the function body
                if body_line.strip() and len(body_line) - len(body_line.lstrip()) <= indent_to_remove:
                    # We've exited the function, don't modify this line
                    break
                    
                # Remove the common indentation
                if body_line.strip():  # Only process non-empty lines
                    fixed_lines.append(body_line[indent_to_remove:])
                else:
                    fixed_lines.append(body_line)  # Preserve empty lines
                i += 1
        else:
            # No indentation issues, keep the line as is
            fixed_lines.append(line)
            i += 1
    
    # Write the fixed content back
    with open(file_path, 'w') as f:
        f.writelines(fixed_lines)


def main():
    """Process all Python files in the directory"""
    print("Fixing indentation in restructured Python files...")
    
    # Find all Python files
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                fix_file(os.path.join(root, file))
    
    print("Indentation fixing complete!")


if __name__ == "__main__":
    main()