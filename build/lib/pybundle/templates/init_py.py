def init_py(params):
    return {
        "location": f'{params["module"]}/__init__.py',
        "content": """
# This is the main file.
def main():
    # Write your code in here.
"""
    }