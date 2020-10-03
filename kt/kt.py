#! /usr/bin/python
import sys
import os

# The base path of the KW workspace
KT_WORKSPACE = "/mnt/onboard/kt"

def _workspace():
    print(KT_WORKSPACE)

def _workspace_open():
    pass

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
    exit(1)