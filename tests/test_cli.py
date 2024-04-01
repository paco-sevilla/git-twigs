# Copyright 2024: The `git-twigs` authors
#
# This file is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License, version 2 (GNU GPLv2).This software is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY. See the `LICENSE` file for more details.
#
"""Tests for the `cli` module."""

from click.testing import CliRunner

from git_twigs import cli


def test_main() -> None:
    """Test the `main` entry point."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "git-twig - List, create, or delete twigs." in result.output
