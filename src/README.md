# B3D Tools

## What is this module?

This is a python module.

Python is nice of several reasons:
* Opensource
* Free
* Extensible
* Readable
* Extensible

## How to install this module?

To install this as code in your python project:

    % python3 -m build
    % pip install dist/b3dtools-0.1.1-py3-none-any.whl --force-reinstall

alernatively you can install this module directly from github:

    % pip install git+https://github.com/kbotnen/b3dtools.git
    
To use the module after it is installed:

    % python
    >>> from b3dtools import b3d
    >>> help(b3d)
    >>> b3d.b3d_dicethrow(10)
    [3, 3, 4, 3, 5, 4, 2, 3, 5, 1]
    >>> quit()

The modules is just an example of how to share your code as a module.