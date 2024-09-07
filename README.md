# Mongodb Python Hackpack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Python

MongoDB Python Hackpack runs on Python Version 3.8 and higher. Please ensure you have Python installed.

## Poetry

This project is built using [Poetry](https://python-poetry.org), a Python package and dependency manager. Please ensure you have Poetry installed using the [official installation guide](https://python-poetry.org/docs/#installation). You can also install Poetry via the following command:

```bash
# Linux, MacOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -
```

## PyMongo

This project uses [PyMongo] (https://pymongo.readthedocs.io/en/stable/index.html), a Python distribution containing tools for working with [MongoDB](https://www.mongodb.com/). 

## Environment Variables

The following environment variables are required and must be stored in an `.env` file:
```bash
MONGODB_URI=
```

### Connection to MongoDB

The `MONGODB_URI` env variable is a [MongoDB connection string](https://www.mongodb.com/docs/guides/atlas/connection-string/).

## Commands

### Dependencies

```bash
# Install dependencies
poetry install

# Add dependency
poetry add <dependency>

# Remove dependency
poetry remove <dependency>
```

### Running the Code Locally

```bash
poetry run app
```

### Formatting Code via YAPF

```bash
# Rewrite code recursively with proper formatting
poetry run yapf -ir app

# Show formatting differences recursively
poetry run yapf -dr app
```

### Linting Code via Pylint

```bash
poetry run pylint app
```

### Build the Code

```bash
poetry build
```