import yaml
import os
from .templates import init_py, main_script, setup, reqs, pyb_yml

def init(args):
    name = input("Name? ")
    desc = input("Description? ")
    author = input("Author? ")
    version = input("Version? ")
    module = input("Package? ")
    script = input("Executable name? ")
    while module == script:
        print("\33[31mCannot use module name as executable name\33[0m")
        module = input("Package? ")
        script = input("Executable name? ")
    params = {
        "name": name,
        "desc": desc,
        "author": author,
        "version": version,
        "module": module,
        "script": script
    }
    try:
        write_template(setup.setup(params))
        write_template(reqs.reqs(params))
        write_template(main_script.main_script(params))
        write_template(pyb_yml.pyb_yml(params))
        os.mkdir(module)
        write_template(init_py.init_py(params))
        write_template(main_script.main_script({"script": module + "/__main__.py", "module": module}))
    except AttributeError as e:
        print(e)

def write_template(tmpl):
    print("W " + tmpl["location"])
    f = open(tmpl["location"], "w")
    f.write(tmpl["content"])
    f.close()