import re
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

# Read the version information from the verion file
VERSION_FILE="labnode_async/_version.py"
VERSION_REGEX = r'^__version__ = [\'"]([^\'"]+)[\'"]$'
with open(VERSION_FILE, 'r') as f:
    version = f.read()
    result = re.search(VERSION_REGEX, version, re.M)
    if result:
        version = result.group(1)
    else:
        raise RuntimeError('No version string found in file %s.', VERSION_FILE)

setup(
   name='labnode_async',
   version=version,
   author='Patrick Baus',
   author_email='patrick.baus@physik.tu-darmstadt.de',
   url='https://github.com/PatrickBaus/LabNode',
   description='An AsyncIO implementation for the Labnode API',
   long_description=long_description,
   classifiers=[
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Topic :: Home Automation',
   ],
   keywords='Labnode API',
   license='GPL',
   license_files=('LICENSE',),
   packages=['labnode_async'],  # same as name
   install_requires=['cobs', 'cbor2', 'pyserial-asyncio'],  # external packages as dependencies
)
