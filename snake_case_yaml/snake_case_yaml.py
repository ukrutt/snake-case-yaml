"""YAML config file parser that accepts snake_case keywords."""

import configargparse
import inflection


def dasherize(prop_name):
    """Convert snake_case to dashes."""
    snake_case = inflection.underscore(prop_name)
    return inflection.dasherize(snake_case)


class SnakeCaseYAMLConfigFileParser(configargparse.YAMLConfigFileParser):
    """YAML config file parser that accepts snake_case keywords.

    Or rather, that converts these to sausage-case.

    Based on idea in https://github.com/bw2/ConfigArgParse/issues/132
    """

    def parse(self, stream):
        """Convert snake_case to dashes in all keys."""
        config = super().parse(stream)
        return {dasherize(key): prop for key, prop in config.items()}
