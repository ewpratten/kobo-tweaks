#! /usr/bin/python
import sys
import os

# The base path of the KW workspace
KT_WORKSPACE = "/mnt/onboard/kt"

def _workspace():
    """Print the abs workspace path"""
    print(KT_WORKSPACE)

def _workspace_open():
    """Create and open the workspace (a writable path)"""

    # Ensure the workspace exists
    if not os.path.exists(KT_WORKSPACE):
        os.mkdirs(KT_WORKSPACE)
        print("Created system workspace directory")
    
    # Move to that dir
    os.chdir(KT_WORKSPACE)
    print("Opened the KT workspace")
    

# Listing of commands to their actions
cli_commands = {
    "ws":_workspace,
    "ws open": _workspace_open
}

# Try to run a command
user_command = " ".join(sys.argv[1:])
if user_command in cli_commands:
    cli_commands[user_command]()
    exit(0)
else:
    print("kt {command}: Unknown command".format(command=user_command))

    # Print a listing of commands
    for command in cli_commands:
        print("kt {command}".format(command=command))
    exit(1)