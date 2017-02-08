#/bin/bash

virtualenv aws
source aws/bin/activate

bin/pip install setuptools

bin/python setup.py test