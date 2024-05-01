from sys import stdout
from printer import Print
from subprocess import PIPE, Popen, run

def run_commands(commands=[]):
    run("clear", shell=True)

    total_commands = len(commands)
    for i, command in enumerate(commands, start=1):
        stdout.write("\033[F\033[K")
        Print.i(f"Executing [{i}/{total_commands}]: {command.description}")
        process = Popen(
            command.command, shell=True, stdout=PIPE,
            stderr=PIPE, text=True, bufsize=1, universal_newlines=True)

        while True:
            stdout_line = process.stdout.readline()
            stderr_line = process.stderr.readline()

            if not stdout_line and not stderr_line:
                break

            stdout.write("\033[F\033[K")
            
            if stdout_line:
                print(stdout_line.strip())

            if stderr_line:
                print(stderr_line.strip())

            Print.i(f"Executing [{i}/{total_commands}]: {command.description}")

        process.stdout.close()
        process.stderr.close()

        return_code = process.poll()
        if return_code:
            stdout.write("\033[F\033[K")
            Print.e(f"Received error when running command '{command.command}'")
            return False
    
    return True
