import os
from pip._internal.commands.install import InstallCommand
def add(args):
    print("Adding to requirements...")
    f = open("requirements.txt", "a")
    f.write(args.pkg + "\n")
    f.close()
    print("Installing...")
    cmd = InstallCommand("install", "")
    cmd.main([args.pkg])