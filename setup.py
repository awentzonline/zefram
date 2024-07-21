import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="zefram",
    version="0.0.1",
    author="Adam Wentz",
    author_email="adam@adamwentz.com",
    description="Boldly seek out new warp field metrics.",
    long_description=read("README.md"),
    license="MIT",
    url="https://github.com/awentzonline/zefram",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'click',
        'numpy',
        'sympy',
    ]
)
