import yaml
from .templates.setup import setup
def init(args):
    name = input("Name? ")
    desc = input("Description? ")
    author = input("Author? ")
    version = input("Version? ")
    module = input("Module? ")
    params = {
        "name": name,
        "desc": desc,
        "author": author,
        "version": version,
        "module": module
    }
    write_template(setup(params))

def write_template(tmpl):
    f = open(tmpl["location"], "w")
    f.write(tmpl["content"])
    f.close()