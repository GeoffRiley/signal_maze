"""Setup configuration for Signal Maze."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="signal_maze",
    version="0.1.0",
    author="Geoff Riley",
    description="A turn-based puzzle game with interconnected components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GeoffRiley/signal_maze",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "signal-maze=signal_maze.cli:main",
        ],
    },
)
