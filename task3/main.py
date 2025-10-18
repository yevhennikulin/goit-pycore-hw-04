import sys, pathlib
from colorama import Fore, Style
# Define a function to visualize directory structure
def visualize_directory_structure(directory_path):
    try:
        # Get the path object
        p = pathlib.Path(directory_path)
        if not p.exists():
            raise FileNotFoundError
        if not p.is_dir():
            raise NotADirectoryError
        #print the current directory
        print(f"{Fore.BLUE}{p.name}/ {Style.RESET_ALL}")
        #define a recursive function to traverse the directory,
        #indent set to 1, since we output the parent directory already
        def recurse_directory(path, indent_level=1):
            # set indent based on the level of recursion
            indent = ' ' * (indent_level * 4)
            # iterate through items in the directory
            for item in path.iterdir():
                # check if the item is a directory or a file and print accordingly
                if item.is_dir():
                    print(f"{indent}{Fore.BLUE}{item.name}/ {Style.RESET_ALL}")
                    recurse_directory(item, indent_level + 1)
                else:
                    print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
        #start the recursion from the given directory path
        recurse_directory(p)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function with the directory path from command line argument
visualize_directory_structure(sys.argv[1])


