from setuptools import setup, findall
import os

def find_scripts(script_dir):
    return [s for s in findall(script_dir) if os.path.splitext(s)[1] != '.pyc']

setup(
    name='jpd',

    version='0.1',

    description='Libraries and scripts I use',

    # The project's main homepage.
    url='https://github.com/jdidion/jpd',

    # Author details
    author='John Didion',
    author_email='code@didion.net',

    # Choose your license
    license='GPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GPL',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    package_dir = { 'jpd' : 'src' },
    
    scripts=find_scripts('bin/')
)