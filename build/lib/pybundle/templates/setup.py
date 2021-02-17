def setup(params):
    return {
        "location": "setup.py",
        "content": f"""
from distutils.core import setup

setup(
    name="{params["name"]}",
    version="{params["version"]}",
    author="{params["author"]}",
    # author_email="",
    # url="",
    description="{params["desc"]}",
    packages=["{params["module"]}"],
    scripts=['{params["script"]}']
)
"""
    }