import subprocess
import os

def clear_cli():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
def ask_to_bool(question):
    do = input(question + " Y / N:\n").lower()
    if do == 'n':
        do = False
        clear_cli()
    elif do == 'y':
        do = True
        clear_cli()
    else:
        print("Unknown: ", do, ", please enter either Y or N")
        ask_to_bool(question)
    return do
