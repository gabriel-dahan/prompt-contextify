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