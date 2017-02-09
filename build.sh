#!/bin/bash

virtualenv aws
source aws/bin/activate

pip install setuptools

python setup.py test

/usr/local/bin/aws-actions list

/usr/local/bin/aws-actions status 1