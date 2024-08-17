"""Example tests."""

import {{ cookiecutter.package_name }}


def test_package_version_p() -> None:
    """Test that package version exists."""
    assert {{ cookiecutter.package_name }}.__version__ != '0.0.0'
