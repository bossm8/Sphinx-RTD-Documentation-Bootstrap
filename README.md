# Sphinx Documentation Template

This is a template to bootstrap documentations based on 
[sphinx](https://www.sphinx-doc.org) and [rtd](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html).

## Usage

* Fork this project into your own namespace.
* Clone the just forked repo. 
* Initialize and watch the project

  ```bash
  make watch
  ``` 

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
