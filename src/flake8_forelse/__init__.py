"""
This file is part of flake8-forelse.

Copyright (C) 2022  Koviubi56

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__version__ = "1.0.0"
__author__ = "Koviubi56"
__email__ = "koviubi56@duck.com"
__license__ = "GNU GPLv3+"
__copyright__ = "Copyright (C) 2022 Koviubi56"
__description__ = (
    "A Flake8 plugin which checks the use of for-else and while-else"
)
__url__ = "https://github.com/koviubi56/flake8-forelse"

import ast
import typing

ERROR_MESSAGE_FORELSE = "FE1 for-else is not allowed"
ERROR_MESSAGE_WHILEELSE = "FE2 while-else is not allowed"


class Flake8ASTErrorInfo(typing.NamedTuple):
    line_number: int
    offset: int
    msg: str
    cls: type


class ForElseVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: typing.List[Flake8ASTErrorInfo] = []

    def visit_For(self, node: ast.For) -> None:
        if node.orelse:
            self.errors.append(
                Flake8ASTErrorInfo(
                    node.lineno,
                    node.col_offset,
                    ERROR_MESSAGE_FORELSE,
                    ForElsePlugin,
                )
            )
        self.generic_visit(node)


class WhileElseVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: typing.List[Flake8ASTErrorInfo] = []

    def visit_While(self, node: ast.While) -> None:
        if node.orelse:
            self.errors.append(
                Flake8ASTErrorInfo(
                    node.lineno,
                    node.col_offset,
                    ERROR_MESSAGE_WHILEELSE,
                    ForElsePlugin,
                )
            )
        self.generic_visit(node)


class ForElsePlugin:
    name = "flake8_forelse"
    version = __version__

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> typing.Generator[Flake8ASTErrorInfo, None, None]:
        errors: typing.List[Flake8ASTErrorInfo] = []

        for_visitor = ForElseVisitor()
        for_visitor.visit(self._tree)
        errors.extend(for_visitor.errors)

        while_visitor = WhileElseVisitor()
        while_visitor.visit(self._tree)
        errors.extend(while_visitor.errors)

        yield from errors
