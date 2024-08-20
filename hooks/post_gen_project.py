# noqa: INP001

"""Cookiecutter post-gen-project hook."""

import shutil
from pathlib import Path

# Remove license folder
shutil.rmtree(Path(Path.cwd().joinpath('license_templates')))
