import os


def move_file(command: str) -> None:
    parsed_command = command.split(" ")
    if len(parsed_command) != 3 or parsed_command[0] != "mv":
        return
    com, source, destination = parsed_command
    if destination[-1] == "/":
        destination = os.path.join(destination, os.path.basename(source))
    if "/" not in destination:
        os.rename(source, destination)
    else:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        os.rename(source, destination)
