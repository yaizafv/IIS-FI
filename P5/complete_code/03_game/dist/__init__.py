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
logic = load_compiled_module("game_logic", "game_logic.cpython-313.pyc")
interface = load_compiled_module("game_user_io", "game_user_io.cpython-313.pyc")
main_f = load_compiled_module("game_main", "game_main.cpython-313.pyc")


# Export modules
__all__ = ["logic", "interface", "main_f"]