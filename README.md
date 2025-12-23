
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

A project making it easy to share your project tree and content with LLMs !

Contextify is a command-line utility designed to bridge the gap between complex local development environments and Large Language Models (LLMs). It flattens your entire directory structure and file contents into a single, well-organized text file, providing the AI with the full context it needs to understand, debug, or extend your project.

---

## Key Features

* **Tree Generation**: Automatically creates a visual representation of your project's directory structure at the top of the file.
* **Recursive Aggregation**: Scans all subdirectories and appends file contents successively.
* **Contextual Headers**: Each file is preceded by its relative path and position, helping the AI understand where the code lives within the architecture.
* **Custom Filtering**: Support for ignoring specific folders (like `node_modules`, `.git`, or `dist`) and file types to keep the context clean and concise.
* **LLM Optimized**: The output format is designed to be easily parsed by models like GPT-4, Claude, or Gemini.

---

## Output Structure

The generated file follows a consistent pattern to ensure maximum readability for the AI:

1. **Project Metadata**: Project name and generation timestamp.
2. **Directory Tree**: A visual map of the project.
3. **File Modules**: For every file, Contextify provides:
    * A clear separator.
    * The full relative file path.
    * The file content wrapped in appropriate Markdown code blocks.

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

## License

This project is licensed under the MIT License.