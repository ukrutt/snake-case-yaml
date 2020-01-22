"""Test snake case YAML."""

import argparse

import configargparse
import pytest

import snake_case_yaml


@pytest.mark.xfail(raises=AssertionError)
@pytest.mark.usefixtures("test_root")
def test_snake_case_fail():
    """The regular YAML parser will cause ConfigArgParse to fail."""
    parser = configargparse.Parser(
        config_file_parser_class=configargparse.YAMLConfigFileParser,
    )
    parser.add_argument("-c", default="config.yaml", is_config_file=True)
    parser.add_argument("--snake-key", default=0.1)
    parser.add_argument("--sausage-key", default=0.2)
    known, unknown = parser.parse_known("")
    assert unknown == []
    assert known == argparse.Namespace(
        snake_key="1.0", sausage_key="2.0", c="config.yaml"
    )


@pytest.mark.usefixtures("test_root")
def test_snake_case_pass():
    """The regular YAML parser will cause ConfigArgParse to fail."""
    parser = configargparse.Parser(
        config_file_parser_class=snake_case_yaml.SnakeCaseYAMLConfigFileParser,
    )
    parser.add_argument("-c", default="config.yaml", is_config_file=True)
    parser.add_argument("--snake-key", default=0.1)
    parser.add_argument("--sausage-key", default=0.2)
    known, unknown = parser.parse_known("")
    assert unknown == []
    assert known == argparse.Namespace(
        snake_key="1.0", sausage_key="2.0", c="config.yaml"
    )
