import pathlib

from setuptools import setup


def dunder_file() -> pathlib.Path:
    try:
        return pathlib.Path(__file__).resolve()
    except Exception:
        try:
            raise ValueError
        except ValueError as exc:
            return pathlib.Path(
                exc.__traceback__.tb_frame.f_code.co_filename
            ).resolve()


readme = (
    (pathlib.Path(dunder_file()) / ".." / "README.md")
    .resolve()
    .read_text(encoding="utf-8")
)

setup(
    name="flake8_forelse",
    version="1.0.0",
    description=(
        "A Flake8 plugin which checks the use of for-else and while-else"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Koviubi56",
    author_email="koviubi56@duck.com",
    maintainer="Koviubi56",
    maintainer_email="koviubi56@duck.com",
    url="https://github.com/koviubi56/flake8-forelse",
    download_url="https://github.com/koviubi56/flake8-forelse/releases",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "License :: OSI Approved :: GNU General Public License v3 or later"
        " (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
    ],
    license="GNU GPLv3+",
    keywords=[
        "flake8",
        "plugin",
        "for",
        "else",
        "forelse",
        "while",
        "whileelse",
    ],
    zip_safe=False,
    install_requires=[],
    entry_points={
        "flake8.extension": [
            "FE = flake8_forelse:ForElsePlugin",
        ],
    },
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/koviubi56/flake8-forelse",
        "Tracker": "https://github.com/koviubi56/flake8-forelse/issues",
    },
)
