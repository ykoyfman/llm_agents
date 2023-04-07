from llm_agents.tools.base import ToolInterface

import subprocess
import sys

def do_install(package: str) -> str:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    return ("Done")

class PipInstallTool(ToolInterface):
    """Tool to install a new pip package"""

    name = "pip install tool"
    description = "Install a new Python package using pip. Input is the name of the package to install."
    
    def use(self, input_text: str) -> str:
        return do_install(input_text)

if __name__ == '__main__':
    print("Install pip package tool implementation")
