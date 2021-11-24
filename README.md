# Sphinx Documentation Template

This is a template to bootstrap documentations based on 
[sphinx](https://www.sphinx-doc.org) and [rtd](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html).

## Usage

* Fork this project into your own namespace.
* Clone the just forked repo.
* Move `.env.template` to `.env`
* Edit `.env` (possible values are documented there)
* Run setup.sh 
  ```bash
  /bin/bash setup.sh
  ``` 
  or 
  ```bash
  chmod 774 setup.sh
  ./setup.sh
  ``` 
  This will install all dependencies and run an initial build. 
* Open the generated documentation 
  ```bash
  xdg-open build/html/index.html
  ```
* For following builds activate the virtual environment and run make
  ```bash
  source venv/bin/activate
  make html
  ```
* Source code can be written either with markdown (`.md`) or with restructured text (`.rst`).
  All source code files are located in `source`.

## Watch

Run `python3 sphinx.py watch`, this will watch for file changes, automatically build and then refresh
the written documentation.

## Configuration and Dependencies

Install new dependencies into the existing environment with pip and add them to the requirements:
```bash
source venv/bin/activate
pip install <dependency>
pip freeze > requirements.txt
```

To configure the packages or modify the template head to `source/conf.py` and read the official sphinx documentation.

## Logos

There are default icons installed in `source/_static/img` override them with your custom ones. If you change
their name make sure to correctly adjust the values in `source/conf.py`.

## Author(s)

* Boss Marco <bossm8@hotmail.ch>
