from setuptools import setup

setup(
    name='aws-recon',
    version='0.3.0',
    description='Tool for performing few basic operations on AWS instances',
    long_description='''
    AWS Recon is a command-line tool written entirely on python.
    It can be used to perform basic operations on AWS instances like listing all the available instances, 
    showing the status of the instance, starting and stopping the instance.

    It uses AWS API to perform the tasks.
    ''',
    author='Bharath Srinivas',
    author_email='cybermaster192@gmail.com',
    scripts=['aws-recon'],
    install_requires=['awscli', 'boto3'],
    packages=['aws'],
    license='MIT',
    platforms=['Ubuntu Trusty', 'Ubuntu Xenial']
)
