# noqa: INP001

"""Cookiecutter pre-prompt hook."""

import shutil
from pathlib import Path

# Copy license_templates folder into project slug
project_dir = Path.cwd()
license_templates_dir = project_dir.joinpath('license_templates')
dst_license_templates_dir = project_dir.joinpath(r'{{ cookiecutter.project_slug }}/license_templates')
shutil.copytree(license_templates_dir, dst_license_templates_dir, dirs_exist_ok=True)
