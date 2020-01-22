"""python-project-template -- my template for new Python programs and libraries
"""

import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

# Get version from VERSION and long description from the README files
with open(os.path.join(HERE, "VERSION")) as version_file:
    VERSION = version_file.read().strip()

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="python-project-template",
    version=VERSION,
    description="Python Project Template",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ukrutt/python-project-template",
    author="Henrik Holm",
    author_email="henrik@forestglenresearch.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8, <4",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # "numpy>=1.16",
        # "scipy>=1.1",
        # "paho-mqtt>=1.4",
    ],
    entry_points={
        # If this isn't a runnable program, you can delete this entry point.
        "console_scripts": [
            "hello_world=python_project_template.main:hello_world",
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
