
from setuptools import setup, find_packages

setup(
    name = "b00705045_IR_pa1",
    version = "1.0",
    packages = find_packages(),
    scripts = ['pa1.py'],
    install_requires = ['docutils>=0.3','nltk>=3.0'],

    package_data = {
        # If any package contains *.txt files, include them:
        '': ['*.txt']
    },

    author = "tsu",
    description = "ir_pa1",
)



