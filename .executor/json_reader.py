from json import load
from printer import Print


class Command():
    def __init__(self, command="", description="") -> None:
        self.command = command
        self.description = description


def get_commands_from_json(file_name=""):
    file_name = file_name.lower()
    if not file_name or not file_name.endswith(".json"):
        Print.e("Please specify a JSON file name")
        return []
    
    file = open(file_name)
    data = load(file)

    commands=[]
    for step in data["steps"]:
        commands.append(Command(step['cmd'], step['description']))

    return commands

