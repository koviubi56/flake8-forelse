# flake8-forelse

[![Hits-of-Code](https://hitsofcode.com/github/koviubi56/flake8-forelse?branch=main)](https://hitsofcode.com/github/koviubi56/flake8-forelse/view?branch=main)
![Codacy grade](https://img.shields.io/codacy/grade/42424fcd258a44f3a0303ca6ca535f67)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/koviubi56/flake8-forelse)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/koviubi56/flake8-forelse/main.svg)](https://results.pre-commit.ci/latest/github/koviubi56/flake8-forelse/main)
![CircleCI](https://img.shields.io/circleci/build/github/koviubi56/flake8-forelse)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![semantic-release](https://img.shields.io/badge/%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)
![GitHub](https://img.shields.io/github/license/koviubi56/flake8-forelse)
![PyPI](https://img.shields.io/pypi/v/flake8-forelse)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-forelse)
![PyPI - Format](https://img.shields.io/pypi/format/flake8-forelse)

A Flake8 plugin which checks the use of for-else and while-else.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flake8-forelse. _[Need more help?](https://packaging.python.org/en/latest/tutorials/installing-packages/)_

```bash
pip install flake8-forelse
```

## Requirements

flake8-forelse requires Python 3.6, and of course flake8.

## Usage

```python
# FE1 for-else is not allowed
for i in range(10):
    print(i)
else:
    print("else")

# FE2 while-else is not allowed
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while-else")
```

## Support

Questions should be asked in the [Discussions tab](https://github.com/koviubi56/flake8-forelse/discussions/categories/q-a).

Feature requests and bug reports should be reported in the [Issues tab](https://github.com/koviubi56/flake8-forelse/issues/new/choose).

Security vulnerabilities should be reported as described in our [Security policy](https://github.com/koviubi56/flake8-forelse/security/policy) (the [SECURITY.md](SECURITY.md) file).

## Contributing
[Pull requests](https://github.com/koviubi56/flake8-forelse/blob/main/CONTRIBUTING.md#pull-requests) are welcome. For major changes, please [open an issue first](https://github.com/koviubi56/flake8-forelse/issues/new/choose) to discuss what you would like to change.

Please make sure to add entries to [the changelog](CHANGELOG.md).

For more information, please read the [contributing guidelines](CONTRIBUTING.md).

## Authors and acknowledgments

A list of nice people who helped this project can be found in the [CONTRIBUTORS file](CONTRIBUTORS).

## License
[GNU GPLv3+](LICENSE)
