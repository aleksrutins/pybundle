import os
import yaml
from .install import install
from .util.config import load_config
def run(args):
    print("\33[1;32mInstalling dependencies...\33[0m")
    install({})
    print("\33[1;32mRunning\33[0m")
    os.system(f"python3 {load_config()['script']}")