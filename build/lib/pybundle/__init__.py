#!/usr/bin/env python3
import yaml
import argparse
from .install import install
from .init import init
from .add import add
from .run import run

def main():
    argparser = argparse.ArgumentParser(prog="pybundle", description="A project-level package manager for PyPI packages", epilog="This package manager has Super Goat Powers")

    subparsers = argparser.add_subparsers(dest="subparser")

    install_parser = subparsers.add_parser("install")
    install_parser.set_defaults(func=install)

    init_parser = subparsers.add_parser("init")
    init_parser.set_defaults(func=init)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("pkg")
    add_parser.set_defaults(func=add)
    
    run_parser = subparsers.add_parser("run")
    run_parser.set_defaults(func=run)

    args = argparser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        argparser.print_usage()