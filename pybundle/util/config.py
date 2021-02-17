import yaml
def load_config():
    f = open("pyb.yml", "r")
    return yaml.safe_load(f)