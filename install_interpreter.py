import os
import sys

# Add the parent directory of the rUv-dev repository to the system path
repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(repo_dir)

# Import the open_interpreter_config module
from open_interpreter_config import configure_open_interpreter

# Call the configure_open_interpreter function
configure_open_interpreter()
