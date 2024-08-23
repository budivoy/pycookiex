"""Tests for baking and setting up the project using cookiecutter templates.

This module contains tests that validate the baking process of a cookiecutter template,
ensuring that the generated project structure is correct and that it can be installed and set up successfully.
"""

import os
import shlex
import subprocess
from collections.abc import Generator, Mapping, Sequence
from contextlib import contextmanager
from pathlib import Path
from shutil import rmtree
from typing import Any

from pytest_cookies.plugin import Cookies  # Importing Cookies type for annotation


@contextmanager
def exec_inside_dir(dirpath: Path) -> Generator[None, None, None]:
  """Execute code from inside the given directory.

  Args:
      dirpath: Path of the directory the command is being run.

  """
  old_path = Path.cwd()
  try:
    os.chdir(dirpath)
    yield
  finally:
    os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(
  cookies: Cookies, *args: Sequence[str], **kwargs: Mapping[str, str | None]
) -> Generator[Any, None, None]:
  """Delete the temporal directory that is created when executing the tests.

  Args:
      cookies: Cookie to be baked and its temporal files will be removed.
      *args: Positional arguments to be passed to the bake function.
      **kwargs: Keyword arguments to be passed to the bake function.

  Yields:
      The result of the bake operation.

  """
  result = cookies.bake(*args, **kwargs)
  try:
    yield result
  finally:
    rmtree(Path(result.project))


def run_inside_dir(command: str, dirpath: Path) -> int:
  """Run a command from inside a given directory, returning the exit status.

  Args:
      command: Command that will be executed.
      dirpath: Path of the directory the command is being run.

  Returns:
      int: The exit status of the command.

  """
  with exec_inside_dir(dirpath):
    return subprocess.check_call(shlex.split(command))  # noqa: S603


def check_output_inside_dir(command: str, dirpath: Path) -> bytes:
  """Run a command from inside a given directory, returning the command output.

  Args:
      command: Command that will be executed.
      dirpath: Path of the directory the command is being run.

  Returns:
      bytes: The output of the command.

  """
  with exec_inside_dir(dirpath):
    return subprocess.check_output(shlex.split(command))  # noqa: S603


def test_bake_with_defaults_p(cookies: Cookies) -> None:
  """Test cookie bake with default values."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = [f.basename for f in result.project.listdir()]
    assert 'README.md' in found_toplevel_files
    assert 'pyproject.toml' in found_toplevel_files


def test_bake_and_install_p(cookies: Cookies) -> None:
  """Test cookie bake and intall."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert run_inside_dir('poetry install', result.project) == 0


def test_bake_and_run_tests_p(cookies: Cookies) -> None:
  """Test cookie bake and run tests."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert run_inside_dir('poetry install --with dev', result.project) == 0
    assert run_inside_dir('poetry run pytest', result.project) == 0


def test_bake_and_run_lint_p(cookies: Cookies) -> None:
  """Test cookie bake and run lint."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert run_inside_dir('poetry install --with dev', result.project) == 0
    assert run_inside_dir('poetry run ruff check', result.project) == 0


def test_bake_and_run_format_p(cookies: Cookies) -> None:
  """Test cookie bake and run format."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert run_inside_dir('poetry install --with dev', result.project) == 0
    assert run_inside_dir('poetry run ruff format', result.project) == 0


def test_bake_and_run_precommit_p(cookies: Cookies) -> None:
  """Test cookie bake and run pre-commit."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert run_inside_dir('poetry install --with dev', result.project) == 0
    assert run_inside_dir('git init', result.project) == 0
    assert run_inside_dir('git add .', result.project) == 0
    assert run_inside_dir('poetry run pip install pre-commit', result.project) == 0
    assert run_inside_dir('poetry run pre-commit run -a', result.project) == 0


def test_bake_and_build_docs_p(cookies: Cookies) -> None:
  """Test cookie bake and build docs."""
  with bake_in_temp_dir(cookies) as result:
    assert result.project.isdir()
    assert run_inside_dir('poetry install --with dev', result.project) == 0
    assert run_inside_dir('poetry run mkdocs build --strict --config-file docs/mkdocs.yml', result.project) == 0
