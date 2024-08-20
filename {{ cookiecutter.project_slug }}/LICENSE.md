{% if cookiecutter.license == "MIT" %}
{%- include 'license_templates/LICENSE-MIT.md' -%}
{% elif cookiecutter.license == "Apache-2.0" %}
{%- include 'license_templates/LICENSE-Apache-2.0.md' -%}
{% elif cookiecutter.license == "GPL-3.0" %}
{%- include 'license_templates/LICENSE-GPL-3.0.md' -%}
{% endif -%}
