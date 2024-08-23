# noqa: INP001

"""MkDocs hooks.

List of hooks:
- Copy extra files to docs directory: copy_extra_files
- Update absolute links from relative to absolute: update_links
"""

import logging
import shutil
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig

log = logging.getLogger('mkdocs')


def copy_extra_files(config: MkDocsConfig) -> list[Path]:
  """Copy extra Markdown files to the docs directory.

  Args:
      config: MkDocs configuration.

  Returns:
      list[Path]: List of paths to the copied files.
  """
  md_file_to_copy = config['extra'].get('md_file_to_update_links', '')
  docs_dir = Path(config['docs_dir'])
  copied_files: list[Path] = []

  log.info('Following Markdown files will be copied to docs dir: %s', md_file_to_copy)

  if not docs_dir.exists():
    log.error('Cannot access docs_dir %s', docs_dir)
    return copied_files

  for file_path in md_file_to_copy:
    src_path = Path(file_path)
    if src_path.exists():
      dest_file_path = docs_dir.joinpath(file_path)
      shutil.copy(src_path, dest_file_path)
      copied_files.append(dest_file_path)
      log.info('Copied %s -> %s', src_path, dest_file_path)
    else:
      log.warning('File not found: %s. Check mkdocs.yml extra', file_path)

  return copied_files


def update_links(file_paths: list[Path]) -> None:
  """Update links from absolute to relative in the copied files.

  Args:
      file_paths: List of paths to the files to update.

  """
  for file_path in file_paths:
    if file_path.exists():
      with file_path.open('r', encoding='utf-8') as file:
        content = file.read()

      # Replace '(./docs/docs/' with '(./'
      modified_content = content.replace('(./docs/docs/', '(./')

      with file_path.open('w', encoding='utf-8') as file:
        file.write(modified_content)

      log.info('Modified links in %s', file_path)
    else:
      log.warning('File not found during link update: %s', file_path)


def remove_extra_files(config: MkDocsConfig) -> None:
  """Remove extra files that were copied to docs_dir.

  Args:
      config: MkDocs configuration.

  """
  md_file_to_remove = config['extra'].get('md_file_to_update_links', '')
  docs_dir = Path(config['docs_dir'])

  log.info('Following Markdown files will be removed from docs dir: %s', md_file_to_remove)

  for file_path in md_file_to_remove:
    dest_file_path = docs_dir.joinpath(file_path)

    if dest_file_path.exists():
      dest_file_path.unlink()
      log.info('Removed: %s', dest_file_path)
    else:
      log.warning('File not found: %s. Check mkdocs.yml extra', dest_file_path)


def on_pre_build(config: MkDocsConfig) -> None:
  """Run when global on-pre-build event triggered."""
  log.info('in: [on_pre_build]')
  copied_files = copy_extra_files(config)
  update_links(copied_files)
  log.info('out: [on_pre_build]')


def on_post_build(config: MkDocsConfig) -> None:
  """Run when global on-post-build event triggered."""
  log.info('in: [on_post_build]')
  remove_extra_files(config)
  log.info('out: [on_post_build]')
