from mindinsight._version import VERSION
from mindinsight.modelarts import notebook

__version__ = VERSION
__version_info__ = tuple(VERSION.split('.'))

__all__ = [
    '__version__',
    '__version_info__'
]


def load_ipython_extension(ipython):
    """
    IPython API entry point.

    Only intended to be called by the IPython runtime.

    See:
       The IPython extension guide.
    """
    notebook.notebook_load_ipython_extension(ipython)
