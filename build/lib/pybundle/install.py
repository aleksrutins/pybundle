import os
from pip._internal.commands.install import InstallCommand

def install(args):
    cmd = InstallCommand("install", "")
    cmd.main(["-r", "requirements.txt"])