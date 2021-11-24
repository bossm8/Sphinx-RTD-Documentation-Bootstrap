#!/bin/bash
set -eu

if [ ! -f .env ]; then
  echo "ERROR: Please copy .env.template to .env and adjust the configuration"
  exit 1
fi

source .env

if [ ! -d venv ]; then
  python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt

sed -i -e "s|<GITLAB_HOST>|${GITLAB_HOST}|g" \
       -e "s|<REPO_URI>|${REPO_URI}|g" \
       -e "s/<AUTHORS>/${AUTHORS}/g" \
       -e "s/<PROJECT_NAME>/${PROJECT_NAME}/g" \
       -e "s/<YEAR>/$(date +%Y)/g" \
       source/conf.py

make html
