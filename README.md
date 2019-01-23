# BDD Lab (Social Network)

This is the source material for the BDD lab.

The goal of this lab is to show how to use human readable specifications to
drive the development of a system - by using [behave](https://github.com/behave/behave), the cucumber-clone BDD framework for Python,
to make the specifications into automated tests.

Instructions on how to do this lab can be found in the
[exercises repository](https://github.com/ONSdigital/onse-training-exercises/blob/master/onse-lab-bdd.md).

### Development Setup

Make sure you have the latest version of Python installed (currently 3.7.1) from
the [Python website](https://www.python.org/downloads/release/python-371/).

From within the repository folder, please install the following in order to run
the project:

```bash
# install the dependencies from Pipfile:
pipenv install --dev

# activate this project's virtualenv:
pipenv shell
```

Pipenv "automatically creates and manages a virtualenv for your projects, as
well as adds/removes packages from your Pipfile as you install/uninstall
packages. It also generates the ever-important Pipfile.lock, which is used to
produce deterministic builds." [1](https://pipenv.readthedocs.io/en/latest/)


## Running tests

The following commands can be executed inside your `pipenv shell`.

### Style & Linting

```bash
flake8
```

### Unit Tests

```bash
python -m pytest
```

### Acceptance Tests (features)

```bash
behave
```

## PyCharm Run Configuration

Add a run configuration of type `Python tests -> pytest` with the following
settings:

![PyCharm Test Config](pycharm-test-config.png)

**REMARK**:

The BDD support is available only in the PyCharm Professional Edition, not in
the Community Edition.
