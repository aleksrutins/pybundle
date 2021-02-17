def main_script(params):
    return {
        "location": params["script"],
        "content": f"""#!/usr/bin/env python3
from {params["module"]} import main
main()
"""
    }