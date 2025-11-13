import sys
import importlib.util
from pathlib import Path

# Helper function to load .pyc files
def load_compiled_module(name, pyc_filename):
    pyc_path = Path(__file__).parent / "__pycache__" / pyc_filename
    spec = importlib.util.spec_from_file_location(name, pyc_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

# Load modules (the order is important)
user_io = load_compiled_module("user_io", "user_io.cpython-313.pyc")
areas_logic = load_compiled_module("areas_logic", "areas_logic.cpython-313.pyc")
areas_main = load_compiled_module("areas_main", "areas_main.cpython-313.pyc")
vectors_logic = load_compiled_module("vectors_logic", "vectors_logic.cpython-313.pyc")
vectors_main = load_compiled_module("vectors_main", "vectors_main.cpython-313.pyc")


# Export modules
__all__ = ["areas_logic", "areas_main", "user_io", "vectors_logic", "vectors_main"]