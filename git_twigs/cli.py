"""CLI entry points for git-twigs."""

import click


@click.group()
def main():
    """git-twig - List, create, or delete twigs."""
