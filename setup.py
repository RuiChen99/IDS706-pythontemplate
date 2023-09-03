"""Python setup.py for ids706_pythontemplate package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("ids706_pythontemplate", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ids706_pythontemplate",
    version=read("ids706_pythontemplate", "VERSION"),
    description="Awesome ids706_pythontemplate created by RuiChen99",
    url="https://github.com/RuiChen99/IDS706-pythontemplate/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="RuiChen99",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["ids706_pythontemplate = ids706_pythontemplate.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
