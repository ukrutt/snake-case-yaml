# Snake Case YAML

Extension to ConfigArgParse with support for YAML files that use
`snake_case` keys.  These don't work well with `configargparse`, since
it expects keys to be in `sausage-case` format.


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
