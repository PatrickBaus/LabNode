[![pylint](https://github.com/PatrickBaus/labnode_async/actions/workflows/pylint.yml/badge.svg)](https://github.com/PatrickBaus/labnode_async/actions/workflows/pylint.yml)
[![PyPI](https://img.shields.io/pypi/v/labnode_async)](https://pypi.org/project/labnode_async/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/labnode_async)
![PyPI - Status](https://img.shields.io/pypi/status/labnode_async)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# LabNode
This is the Python3 AsyncIO API library for the [Labnode](https://github.com/TU-Darmstadt-APQ/Labnode_PID) system.

The library is fully type-hinted.

## Setup
To install the library in a virtual environment (always use venvs with every project):

```bash
python3 -m venv env  # virtual environment, optional
source env/bin/activate
pip install labnode_async
```

## Usage
This library makes use of asynchronous context managers to hide all connection related stuff and
also handle cleanup. By the way: Context managers are great!

Initialize the GPIB adapter
```python
from labnode_async import IPConnection
# Create a device and start coding
async with IPConnection("192.1680.0.2") as device:
    # Add your code here
    ...
```

See [examples/](examples/) for more working examples.

## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the
[tags on this repository](https://github.com/PatrickBaus/labnode_async/tags).

## Documentation
I use the [Numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) style for documentation and
[Sphinx](https://www.sphinx-doc.org/en/master/index.html) for compiling it.

## Authors

* **Patrick Baus** - *Initial work* - [PatrickBaus](https://github.com/PatrickBaus)

## License


This project is licensed under the GPL v3 license - see the [LICENSE](LICENSE) file for details
