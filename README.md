# Project template for Python projects

Folder structure, setup file, CI integration, etc. for a generic Python project

## TO USE

 - Clone this project and delete the .git directory, or simply click the "Use this template" button on https://github.com/ukrutt/python-project-template.
 - Search for python-project-template and replace with the name of your new project

 - Search for python_project_template and replace with the name of your new program (subtly different).  NOTE: this includes the folder.

 - DELETE this section.


## Installation

I like to use pyenv to specify a Python version

    % eval "$(pyenv init -)"
    % python3 --version
    3.8.1
    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install .


## Development

    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install -r requirements-dev.txt
