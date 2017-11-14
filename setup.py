from setuptools import setup

setup(
    name='aws-tool',
    version='1.2.0',
    description='Tool for performing few aws on AWS instances',
    long_description='''
    AWS Tool is a command-line tool written entirely on python.
    It can be used to perform basic operations on AWS instances like listing all the available instances, 
    showing the status of the instance, starting and stopping the instance.

    It uses AWS API to perform the tasks.
    ''',
    author='Bharath Srinivas',
    author_email='bharath@screen-magic.com',
    scripts=['aws-tool'],
    install_requires=['awscli', 'boto3'],
    packages=['aws'],
    license='MIT',
    platforms=['Ubuntu Trusty', 'Ubuntu Xenial']
)
