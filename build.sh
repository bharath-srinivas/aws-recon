#!/bin/bash

virtualenv aws
source aws/bin/activate

pip install setuptools

python setup.py test

aws-actions list

aws-actions status 1