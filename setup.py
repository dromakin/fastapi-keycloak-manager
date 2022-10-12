"""  
setup.py  
  
created by dromakin as 12.10.2022  
Project fastapi-keycloak  
"""

__author__ = 'dromakin'
__maintainer__ = 'dromakin'
__credits__ = ['dromakin', ]
__copyright__ = "Echelon, Inc, 2022"
__status__ = 'Development'
__version__ = 20221012



# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="FastAPI Keycloak Manager",
    version="1.0.0",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://fastapi-keycloak-manager.readthedocs.io/",
    author="Dmitriy Romakin",
    author_email="dvromakin@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=['fastapi_keycloak_manager']),
    include_package_data=True,
    install_requires=["numpy"]
)