#!/usr/bin/env python3
import os
os.system("") # https://stackoverflow.com/a/64431034

import yaml
import argparse
from .install import install
from .init import init

argparser = argparse.ArgumentParser(prog="pybundle", description="A project-level package manager for PyPI packages", epilog="This package manager has Super Goat Powers")

subparsers = argparser.add_subparsers(dest="subparser")

install_parser = subparsers.add_parser("install")
install_parser.add_argument("name")
install_parser.set_defaults(func=install)

init_parser = subparsers.add_parser("init")
init_parser.set_defaults(func=init)

args = argparser.parse_args()
args.func(args)