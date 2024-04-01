# Copyright 2024: The `git-twigs` authors
#
# This file is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License, version 2 (GNU GPLv2).This software is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY. See the `LICENSE` file for more details.
#
"""CLI entry points for git-twigs."""

import click


@click.group()
def main() -> None:
    """git-twig - List, create, or delete twigs."""
