from setuptools import setup

setup(
    name='aws-actions',
    version='1.0',
    description='Tool for starting and stopping AWS instances',
    author='Bharath Srinivas',
    author_email='bharath@screen-magic.com',
    scripts=['bin/aws-actions'],
    install_requires=['setuptools', 'awscli', 'boto3'],
    packages=['functions'],
)
