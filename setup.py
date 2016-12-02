""" IHCAPY: immunohistochemistry analysis tool in python """
from setuptools import setup, find_packages

def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        result = f.read().splitlines()
    return result


def get_long_description():
    with open('README.md') as f:
        result = f.read()
    return result

setup(
    name='ichapy',
    version='0.0.1',
    url='https://github.com/ds2643/ichapy',
    author='David Shaked',
    author_email='ds2643@columbia.edu',
    description='immunohistochemistry analysis tool',
    long_description=get_long_description(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any'
)
