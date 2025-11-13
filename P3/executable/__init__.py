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
medical_report_main = load_compiled_module("medical_report_main", "medical_report_main.cpython-313.pyc")
cypher_main = load_compiled_module("cypher_main", "cypher_main.cpython-313.pyc")

# Export modules
__all__ = ["medical_report_main", "cypher_main"]