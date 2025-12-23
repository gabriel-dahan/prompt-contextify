Project tree: 
        ├── .gitignore
        ├── LICENSE
        ├── README.md
        ├── example_this_project.md
        ├── prompt_contextify/
        │   ├── __init__.py
        │   ├── main.py
        │   └── reader.py
        └── pyproject.toml

---
### File: .gitignore
---

```text
*.egg-info
__pycache__

.venv
```

---
### File: LICENSE
---

```text
Copyright 2025 Gabriel Dahan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

---
### File: README.md
---

```md

```
  ______                         __                            __      __   ______           
 /      \                       /  |                          /  |    /  | /      \          
/$$$$$$  |  ______   _______   _$$ |_     ______   __    __  _$$ |_   $$/ /$$$$$$  |__    __ 
$$ |  $$/  /      \ /       \ / $$   |   /      \ /  \  /  |/ $$   |  /  |$$ |_ $$//  |  /  |
$$ |      /$$$$$$  |$$$$$$$  |$$$$$$/   /$$$$$$  |$$  \/$$/ $$$$$$/   $$ |$$   |   $$ |  $$ |
$$ |   __ $$ |  $$ |$$ |  $$ |  $$ | __ $$    $$ | $$  $$<    $$ | __ $$ |$$$$/    $$ |  $$ |
$$ \__/  |$$ \__$$ |$$ |  $$ |  $$ |/  |$$$$$$$$/  /$$$$  \   $$ |/  |$$ |$$ |     $$ \__$$ |
$$    $$/ $$    $$/ $$ |  $$ |  $$  $$/ $$       |/$$/ $$  |  $$  $$/ $$ |$$ |     $$    $$ |
 $$$$$$/   $$$$$$/  $$/   $$/    $$$$/   $$$$$$$/ $$/   $$/    $$$$/  $$/ $$/       $$$$$$$ |
                                                                                   /  \__$$ |
                                                                                   $$    $$/ 
                                                                                    $$$$$$/  
```

---

A way to easily to share your project tree and content with LLMs !

Contextify is a command-line utility designed to bridge the gap between complex local development environments and Large Language Models (LLMs). It flattens your entire directory structure and file contents into a single, well-organized text file, providing the AI with the full context it needs to understand, debug, or extend your project.

---

## Key Features

* **Tree Generation**: Automatically creates a visual representation of your project's directory structure at the top of the file.
* **Recursive Aggregation**: Scans all subdirectories and appends file contents successively.
* **Contextual Headers**: Each file is preceded by its relative path and position, helping the AI understand where the code lives within the architecture.
* **Custom Filtering**: Support for ignoring specific folders (like `node_modules`, `.git`, or `dist`) and file types to keep the context clean and concise.
* **LLM Optimized**: The output format is designed to be easily parsed by models like GPT-4, Claude, or Gemini.

---

## Installation

Create a python environment (depending on your OS and python installation) :

```bash
python -m venv .venv # (Windows)
# or
python<version> -m venv .venv # (Linux)
```

```bash
source .venv/Scripts/activate # (Windows)
# or 
source .venv/bin/activate # (Linux)
```

Clone the repository and install dependencies : 

```bash
git clone https://github.com/gabriel-dahan/prompt-contextify.git
cd prompt-contextify
```

```bash
pip install -e .
```

You can now use the `contextify` command **inside of the virtual environment**.

To install it globally, consider using a tool like [pipx](https://github.com/pypa/pipx).

---

## Usage

To generate a context file for your current directory:

```bash
contextify . --output project_context.txt
```

### Options

* `--output, -o`: Specify the name of the resulting text file.
* `--ignore, -i`: List directories or files to exclude from the scan.
* `--depth`: Limit how deep the tree and file scan should go.

---

## Why Contextify?

Modern AI models have increasingly large context windows, but manually uploading dozens of files is tedious and error-prone. Contextify automates this process, ensuring that the AI "sees" the same structure you see in your IDE, leading to more accurate suggestions and better-informed code generation.

---

## What is the output format?

The output file is a markdown file following this format : 

```md
<Project tree structure>

---
### File: <project_file_relative_path>
---
\`\`\`file_language
<code>
\`\`\`

...
```

> LLMs are better at understanding a structured markdown file than other formats because they are frequently trained using Markdown.

---

## License

This project is licensed under the MIT License.
```

---
### File: example_this_project.md
---

```md

```

---
### File: prompt_contextify/__init__.py
---

```py
from .reader import Contextify
```

---
### File: prompt_contextify/main.py
---

```py
from pathlib import Path
import argparse

from . import Contextify

CONTEXTIFY_COMMAND_TEXT = '''

  ______                         __                            __      __   ______           
 /      \                       /  |                          /  |    /  | /      \          
/$$$$$$  |  ______   _______   _$$ |_     ______   __    __  _$$ |_   $$/ /$$$$$$  |__    __ 
$$ |  $$/  /      \ /       \ / $$   |   /      \ /  \  /  |/ $$   |  /  |$$ |_ $$//  |  /  |
$$ |      /$$$$$$  |$$$$$$$  |$$$$$$/   /$$$$$$  |$$  \/$$/ $$$$$$/   $$ |$$   |   $$ |  $$ |
$$ |   __ $$ |  $$ |$$ |  $$ |  $$ | __ $$    $$ | $$  $$<    $$ | __ $$ |$$$$/    $$ |  $$ |
$$ \__/  |$$ \__$$ |$$ |  $$ |  $$ |/  |$$$$$$$$/  /$$$$  \   $$ |/  |$$ |$$ |     $$ \__$$ |
$$    $$/ $$    $$/ $$ |  $$ |  $$  $$/ $$       |/$$/ $$  |  $$  $$/ $$ |$$ |     $$    $$ |
 $$$$$$/   $$$$$$/  $$/   $$/    $$$$/   $$$$$$$/ $$/   $$/    $$$$/  $$/ $$/       $$$$$$$ |
                                                                                   /  \__$$ |
                                                                                   $$    $$/ 
                                                                                    $$$$$$/  
                                                      
'''

def __get_command_args():
    parser = argparse.ArgumentParser(
        description="Contextify: Flatten your project into a single markdown file for LLMs."
    )

    parser.add_argument(
        "path", 
        nargs = "?", 
        default = ".", 
        help = "The directory to scan (default: current directory)."
    )

    parser.add_argument(
        "-o", "--output", 
        default = f"llm_contextify.md", 
        help = "The name of the resulting text file."
    )

    parser.add_argument(
        "-i", "--ignore", 
        nargs = "+", 
        default = [],
        type = list[str], 
        help = "Additional directories or files to exclude."
    )

    parser.add_argument(
        "-if", "--ignore-file",
        default = None,
        type = str,
        help = "Specify a file containing files to ignore (like .gitignore)."
    )

    parser.add_argument(
        "--depth", 
        type = int, 
        default = None, 
        help = "Limit how deep the tree and file scan should go."
    )

    args = parser.parse_args()

    target_path = args.path
    output_filename = args.output
    extra_ignores = args.ignore
    ignore_file = args.ignore_file
    max_depth = args.depth

    return target_path, output_filename, extra_ignores, ignore_file, max_depth

def main():
    print(CONTEXTIFY_COMMAND_TEXT)

    project_path, output_path, ignored, ignore_file, max_depth = __get_command_args()
    project_path = Path(project_path)

    context = Contextify(project_path, ignored, ignore_file, output_path)

    print(f'''
        Project path: {project_path.absolute()}
        Output file: {output_path}
        Ignored matches: {', '.join(context.ignored_strings)}
        Max recursive depth: {max_depth}
    ''')

    print(f'''
        Clear project tree: 
          
{context.project_tree}
    ''')

    # Output file generation
    context.write_output_file()
    print(f'     Output file was generated at {output_path}.')

if __name__ == '__main__':
    print('Wrong way of running Contextify, consider reading README.md.')
```

---
### File: prompt_contextify/reader.py
---

```py
from pathlib import Path
import pathspec

DEFAULT_IGNORED_STRINGS = {'.git', '.venv', '__pycache__', '.idea', '.vscode', 'node_modules', 'dist', 'build', '.env'}

class Contextify(object):

    def __init__(self, rel_path: str | Path, ignored_strings: list[str] | str, ignore_file_path: str | Path, output_path: str | Path) -> None:
        self.path = Path(rel_path)
        self.output_path = Path(output_path)
        self.ignore_file_path = Path(ignore_file_path) if ignore_file_path else None
        
        if isinstance(ignored_strings, str): 
            ignored_strings = [ignored_strings]
        self.ignored_strings = DEFAULT_IGNORED_STRINGS \
                                .union(ignored_strings) \
                                .union(self.__parse_ignore_file())

        self.project_tree = self.__get_project_tree(self.path, indent = ' ' * 8)


    def __is_file_allowed(self, filename: str, patterns: list[str]) -> bool:
        """
        :param filename: Name of the file (with extension)
        :param patterns: A list of patterns (following .gitignore format)
        :return: Returns true if the file is kept, false otherwise.
        :rtype: bool
        """

        spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)
        
        return not spec.match_file(filename)

    def __allowed_items_in(self, items: list[str | Path], sort: bool = True) -> list[str | Path]: 
        """
        :param items: A list of file/folder paths.
        :param sort: Whether to sort the output list or not (default: True).
        :return: Returns a list of file/folder paths matching the allowed file names.
        :rtype: list[str | Path]
        """

        filtered_items = [it for it in items if self.__is_file_allowed(it.name, self.ignored_strings)]

        return sorted(filtered_items) if sort else filtered_items

    def __get_project_tree(self, current_path: str | Path, indent: str = "") -> str:
        """
        :param current_path: Default is the root of the project, then changes recursively.
        :param indent: Adds an indentation string at each of the tree's banches (default: '')
        :return: Returns a clean project tree.
        :rtype: str
        """

        tree_str = ""
        
        items = self.__allowed_items_in(current_path.iterdir())
        
        for i, item in enumerate(items):
            is_last = (i == len(items) - 1)
            connector = "└── " if is_last else "├── "
            
            tree_str += f"{indent}{connector}{item.name}{'/' if item.is_dir() else ''}\n"
            
            if item.is_dir():
                extension = "    " if is_last else "│   "
                tree_str += self.__get_project_tree(item, indent + extension)
                
        return tree_str
    
    def __parse_ignore_file(self) -> set[str]:
        if(not self.ignore_file_path):
            return {}
        
        with open(self.ignore_file_path, 'r') as f:
            lines = f.readlines()

        lines = [l.strip() for l in lines if not (l.strip().startswith('#') or l.strip() == '')]

        return set(lines)
    
    def get_files_markdown_string(self) -> str:
        """
        :return: Returns a formatted string containing the file names, content, etc. (see README).
        :rtype: str
        """

        def get_files_markdown_string_rec(current_path: str | Path) -> str:
            full_string = ''
            
            current_path = Path(current_path)
            
            items = sorted(self.__allowed_items_in(current_path.iterdir()))
            
            for item in items:
                if item.is_file():
                    try:
                        with open(item, 'r', encoding='utf-8') as f:
                            content = f.read()

                        rel_path = item.relative_to(self.path) 
                        
                        lang = item.suffix.lstrip('.') or "text"

                        full_string += f"---\n"
                        full_string += f"### File: {rel_path}\n"
                        full_string += f"---\n\n"
                        full_string += f"```{lang}\n"
                        full_string += f"{content}\n"
                        full_string += f"```\n\n"
                        
                    except (UnicodeDecodeError, PermissionError):
                        continue
                    
                elif item.is_dir():
                    full_string += get_files_markdown_string_rec(item)
                        
            return full_string
        
        return get_files_markdown_string_rec(self.path)

    def write_output_file(self) -> None:
        with open(self.output_path, 'w') as f:
            f.write('Project tree: \n')
            f.write(self.project_tree)
            f.write('\n')
            f.write(self.get_files_markdown_string())
```

---
### File: pyproject.toml
---

```toml
[build-system]
requires = ["setuptools", "wheel", "pathlib", "pathspec"]
build-backend = "setuptools.build_meta"

[project]
name = "contextify"
version = "1.1"
description = "A tool to flatten project context for LLMs"
readme = "README.md"
requires-python = ">=3.7"

[project.scripts]
contextify = "prompt_contextify.main:main"
```

