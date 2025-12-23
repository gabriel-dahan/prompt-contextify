from pathlib import Path

DEFAULT_IGNORED_STRINGS = {'.git', '.venv', '__pycache__', '.idea', '.vscode', 'node_modules', 'dist', 'build', '.env'}

class ProjectReader(object):

    def __init__(self, rel_path: str | Path, ignored_strings: list[str] | str) -> None:
        self.path = rel_path
        
        if isinstance(ignored_strings, str): 
            ignored_strings = [ignored_strings]
        self.ignored_strings = DEFAULT_IGNORED_STRINGS.union(ignored_strings)

        self.project_tree_list = self.__get_project_tree_list(self.path, indent = ' ' * 8)


    def get_file_formatted_content(self, file_path: str | Path) -> str:
        """        
        :param file_path: A path to the file
        :return: Returning the file's content formatted in Markdown :

            relative-path: <file_relative_path>
            content: < ...
                       content
                            ... > 
        :rtype: str
        """

        if isinstance(file_path, str):
            file_path = Path(file_path)

        with open(file_path, 'r') as f:
            self.file_content = f.readlines()
        
        project_relative_path = file_path.relative_to(self.path)

        return f'relative-path: {project_relative_path}\n content: {self.file_content}\n'

    def __get_project_tree_list(self, current_path: str | Path, indent: str = "") -> list[str]:
        """
        :param current_path: Default is the root of the project, then changes recursively.
        :param indent: Adds an indentation string at each of the tree's banches (default: '')
        :param ignore_list: A string or list of strings with comprehensive path (like .gitignore)
        :return: Returning the file's content formatted in Markdown :

            relative-path: <file_relative_path>
            content: < ...
                       content
                            ... > 
        :rtype: str
        """
        tree_str = ""
        
        items = sorted([item for item in current_path.iterdir() if item.name not in self.ignored_strings])
        
        for i, item in enumerate(items):
            is_last = (i == len(items) - 1)
            connector = "└── " if is_last else "├── "
            
            tree_str += f"{indent}{connector}{item.name}\n"
            
            if item.is_dir():
                extension = "    " if is_last else "│   "
                tree_str += self.__get_project_tree_list(item, indent + extension)
                
        return tree_str