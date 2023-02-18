treeplot's documentation!
==============================

|python| |pypi| |docs| |stars| |LOC| |downloads_month| |downloads_total| |license| |forks| |open issues| |project status| |colab| |repo-size| |donate|

.. include:: add_top.add


.. |figd| image:: ../figs/fig_breast_randomforest.png

.. table:: Example treeplot.
   :align: center

   +----------+
   | |figd|   |
   +----------+


``treeplot`` is Python package to easily plot the tree derived from models such as decisiontrees, randomforest and xgboost. Developing explainable machine learning models is becoming more important in many domains. The most popular and classical explainable models are still tree based. Think of decision trees or random forest. The tree that is learned can be visualized and then explained. However, it can be a challange to simply plot the tree. Think of configuration issues with dot files, path locations to graphviz, differences across operating systems, differences across editors such as jupyter notebook, colab, spyder etc. This frustration led to this library, an easy way to plot the decision trees 🌲. It works for Random-forest, decission trees, xgboost and gradient boosting models. Under the hood it makes many checks, downloads graphviz, sets the path and then plots the tree.

-----------------------------------


Treeplot can be used for: **Random-forest**, **Decision trees**, **XGboost** and **Gradient boosting models**:

	* .plot		: Generic function to plot the tree of any of the four models with default settings
	* .randomforest : Plot the randomforest model.
	* .xgboost	: Plot the xgboost model.
	* .LightBM	: Plot the LightBM model.


-----------------------------------

.. note::
	**Your ❤️ is important to keep maintaining this package.** You can `support <https://erdogant.github.io/treeplot/pages/html/Documentation.html>`_ in various ways, have a look at the `sponser page <https://erdogant.github.io/treeplot/pages/html/Documentation.html>`_.
	Report bugs, issues and feature extensions at `github <https://github.com/erdogant/treeplot/>`_ page.

	.. code-block:: console

	   pip install treeplot

-----------------------------------



Content
=======

.. toctree::
   :maxdepth: 1
   :caption: Installation
   
   Installation


.. toctree::
  :maxdepth: 1
  :caption: Tutorials

  Tutorials


.. toctree::
  :maxdepth: 1
  :caption: Plot

  Examples

.. toctree::
  :maxdepth: 1
  :caption: Documentation
  
  Documentation
  Coding quality
  treeplot.treeplot



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`




.. |python| image:: https://img.shields.io/pypi/pyversions/treeplot.svg
    :alt: |Python
    :target: https://erdogant.github.io/treeplot/

.. |pypi| image:: https://img.shields.io/pypi/v/treeplot.svg
    :alt: |Python Version
    :target: https://pypi.org/project/treeplot/

.. |docs| image:: https://img.shields.io/badge/Sphinx-Docs-blue.svg
    :alt: Sphinx documentation
    :target: https://erdogant.github.io/treeplot/

.. |stars| image:: https://img.shields.io/github/stars/erdogant/treeplot
    :alt: Stars
    :target: https://img.shields.io/github/stars/erdogant/treeplot

.. |LOC| image:: https://sloc.xyz/github/erdogant/treeplot/?category=code
    :alt: lines of code
    :target: https://github.com/erdogant/treeplot

.. |downloads_month| image:: https://static.pepy.tech/personalized-badge/treeplot?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month
    :alt: Downloads per month
    :target: https://pepy.tech/project/treeplot

.. |downloads_total| image:: https://static.pepy.tech/personalized-badge/treeplot?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
    :alt: Downloads in total
    :target: https://pepy.tech/project/treeplot

.. |license| image:: https://img.shields.io/badge/license-MIT-green.svg
    :alt: License
    :target: https://github.com/erdogant/treeplot/blob/master/LICENSE

.. |forks| image:: https://img.shields.io/github/forks/erdogant/treeplot.svg
    :alt: Github Forks
    :target: https://github.com/erdogant/treeplot/network

.. |open issues| image:: https://img.shields.io/github/issues/erdogant/treeplot.svg
    :alt: Open Issues
    :target: https://github.com/erdogant/treeplot/issues

.. |project status| image:: http://www.repostatus.org/badges/latest/active.svg
    :alt: Project Status
    :target: http://www.repostatus.org/#active

.. |donate| image:: https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors
    :alt: donate
    :target: https://erdogant.github.io/treeplot/pages/html/Documentation.html#

.. |colab| image:: https://colab.research.google.com/assets/colab-badge.svg
    :alt: Colab example
    :target: https://erdogant.github.io/treeplot/pages/html/Documentation.html#colab-notebook

.. |repo-size| image:: https://img.shields.io/github/repo-size/erdogant/treeplot
    :alt: repo-size
    :target: https://img.shields.io/github/repo-size/erdogant/treeplot

.. include:: add_bottom.add
