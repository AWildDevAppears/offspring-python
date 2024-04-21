# Offspring Engine

A very simple, expandable engine for building games.
This engine is written in python, although I may change this in the future for V2.

# What we use:

* Poetry
* TinyDB
* PKL
* Toga

# Setup

To use this project, you will need poetry installed.
See [poetry's documentation](https://python-poetry.org/docs/main/) to get it installed.

## Building the project

Now we have poetry installed we need to get our dependencies installed.

Run:

```
poetry install
```

to install the dependencies.
To run the project, call

```
poetry run python offspringengine
```

## Formatting

In order to format the files you will need to run

```
poetry run lint
```
