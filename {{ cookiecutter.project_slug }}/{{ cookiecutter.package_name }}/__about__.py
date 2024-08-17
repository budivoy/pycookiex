import toml
from pathlib import Path

# Load pyproject.toml
pyproject_path = Path("pyproject.toml")
pyproject_data = toml.load(pyproject_path)

# Extract information
project_info = pyproject_data.get("tool", {}).get("poetry", {})

__version__ = project_info.get("version", "0.0.0")
