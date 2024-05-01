from glob import glob
from json import load
from printer import Print


def print_commands(parent_directory_path=""):
    if not parent_directory_path:
        Print.i("Specify a parent directory to check JSON files.")
        return

    json_files = glob(f"{parent_directory_path}/**/*.json", recursive=True)
    for file_path in json_files:
        file = open(file_path)
        data = load(file)
        Print.i(f"{data["name"]} - {data["description"]}")

if __name__ == "__main__":
    print_commands(".cmds")
