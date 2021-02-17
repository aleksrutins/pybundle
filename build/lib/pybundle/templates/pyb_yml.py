def pyb_yml(params):
    return {
        "location": "pyb.yml",
        "content": f"""
# pyb.yml
# This is the PyBundle configuration file.
name: {params["name"]} # Project name
script: {params["script"]} # Main script path (for 'pyb run')
"""
    }