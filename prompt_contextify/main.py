from pathlib import Path
import argparse

from . import ProjectReader

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

    project_path_raw, output, ignores, ignore_file, max_depth = __get_command_args()
    project_path = Path(project_path_raw)

    pr = ProjectReader(project_path, ignores)

    print(f'''
        Project path: {project_path.absolute()}
        Output file: {output}
        Ignored matches: {', '.join(pr.ignored_strings)}
        Max recursive depth: {max_depth}
    ''')

    print(f'''
        Clear project tree: 
          
{pr.project_tree_list}
    ''')


if __name__ == '__main__':
    print('Wrong way of running Contextify, consider reading README.md.')