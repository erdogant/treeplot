Installation
################


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install treeplot

    # Force update to latest version
    pip install -U treeplot


Github source
************************************

Install directly from github source (beta versions):

.. code-block:: console

    pip install git+https://github.com/erdogant/treeplot



Graphviz
************************************

The ``treeplot`` package contains the required graphviz libraries and it should work out of the box for both Windows
and Unix machines. However, in some cases it does require a manual installation of the graphviz package.
Binaries for graphviz can be downloaded from the graphviz project homepage, and the Python wrapper installed from pypi
with pip install graphviz.

If you use the conda package manager, the graphviz binaries and the python package can be installed with conda install python-graphviz.

.. code-block:: console

    conda install python-graphviz

If you use the pip package manager, try the Python wrapper installed from Pypi.

.. code-block:: console

    pip install graphviz

An alternative example is to download and install this for Unix machines:

.. code-block:: console

    sudo apt install python-pydot python-pydot-ng graphviz
    # or 
    sudo apt install graphviz

For Mac OS install it as following:

.. code-block:: console

    brew install graphviz


Uninstalling
################


Remove installation
**********************

Note that the removal of the environment will also remove the ``treeplot`` installation.

.. code-block:: console

    # Install from Pypi:
    pip uninstall treeplot



.. include:: add_bottom.add