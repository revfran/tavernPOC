import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "OpenWeatherAPItest",
    version = "0.0.1",
    author = "revfran",
    packages=[ 'OpenWeatherAPItest/tests']
)
