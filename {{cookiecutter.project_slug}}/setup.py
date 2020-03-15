#!/usr/bin/env python3

"""The setup script."""

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent

with open(here / "{{ cookiecutter.project_src_dir }}" / "VERSION") as version_file:
    version = version_file.read().strip()


with open("README.md") as readme_file:
    readme = readme_file.read()


requirements = ["yaqd-core"]

extra_requirements = {"dev": ["black", "pre-commit"]}

{%- set license_classifiers = {
    "GNU Lesser General Public License v3 (LGPL)": "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "MIT license": "License :: OSI Approved :: MIT License",
    "BSD license": "License :: OSI Approved :: BSD License",
    "ISC license": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU General Public License v3 (GPL)": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}
extra_files = {"{{ cookiecutter.project_src_dir }}": ["VERSION"]}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        "console_scripts": [
            "yaqd-{{ cookiecutter.first_daemon_kind }}={{ cookiecutter.project_src_dir }}.{{ cookiecutter.first_daemon_module }}:{{ cookiecutter.class_name }}.main",
        ],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data=extra_files,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_src_dir }}", "{{ cookiecutter.project_src_dir }}.*"]),
    url="https://gitlab.com/{{ cookiecutter.gitlab_org }}/{{ cookiecutter.project_slug }}",
    version=version,
    zip_safe=False,
)
