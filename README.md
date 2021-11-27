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

### Custom Variables

The [breadcrumbs.html](https://github.com/readthedocs/sphinx_rtd_theme/blob/master/sphinx_rtd_theme/breadcrumbs.html) 
template has been simplified and has now the following variables:

`display_link`: If a custom url should be displayed (else `show_source`)

`display_url`: The url to place in the 'href'

`display_icon`: The icon to show in the link, these can be any from [fontawesome](https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free)
free. Just the name is needed, the class will be rendered as `class="fa fa-{{display_icon}}`.

## Logos

There are default icons installed in `source/_static/img` override them with your custom ones. If you change
their name make sure to correctly adjust the values in `source/conf.py`.

## Author(s)

* Boss Marco <bossm8@hotmail.ch>
