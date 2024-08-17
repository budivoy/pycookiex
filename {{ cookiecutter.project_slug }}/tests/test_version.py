import {{ cookiecutter.package_name }}

def test_package_version():
    assert {{ cookiecutter.package_name }}.__version__ != '0.0.0'
