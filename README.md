# Snake Case YAML

Extension to `ConfigArgParse` (https://github.com/bw2/ConfigArgParse) with support for YAML files that use `snake_case` keys.  These don't work well with `configargparse`, since it expects keys to be in `sausage-case` format.

Inspired by https://github.com/bw2/ConfigArgParse/issues/132


## Installation

I like to use pyenv to specify a Python version

    % eval "$(pyenv init -)"
    % python3 --version
    3.7.6
    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install .


## Development

    % python3 -m venv .venv
    % . .venv/bin/activate
    % pip install --upgrade pip
    % pip install -r requirements-dev.txt
