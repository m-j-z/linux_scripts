from sys import argv
from printer import Print
from json_reader import get_commands_from_json
from os import path
from step_logging import run_commands

if __name__ == "__main__":
    if not argv[1:]:
        Print.e("Please specify a JSON file or use help.")
    else:
        arg = argv[1]
        if argv[1].lower() == "help":
            Print.s("HELPPPPP")
        elif not argv[1].lower().endswith(".json"): 
            Print.e("Please specify a JSON file.")
        elif not path.isfile(argv[1]):
            Print.e(f"JSON file not found. Looking for {argv[1]} but could not find it.")
        else:
            commands = get_commands_from_json(argv[1])
            is_ok = run_commands(commands)
            if is_ok:
                Print.s(f"Successfully ran script. Exiting.")
            else:
                Print.e(f"Failed to run script. Exiting.")
