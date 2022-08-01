treeplot's documentation!
==============================

``treeplot`` is Python package to easily plot the tree derived from models such as decisiontrees, randomforest and xgboost. Developing explainable machine learning models is becoming more important in many domains. The most popular and classical explainable models are still tree based. Think of decision trees or random forest. The tree that is learned can be visualized and then explained. However, it can be a challange to simply plot the tree. Think of configuration issues with dot files, path locations to graphviz, differences across operating systems, differences across editors such as jupyter notebook, colab, spyder etc. This frustration led to this library, an easy way to plot the decision trees 🌲. It works for Random-forest, decission trees, xgboost and gradient boosting models. Under the hood it makes many checks, downloads graphviz, sets the path and then plots the tree.


Treeplot can plot the tree for Random-forest, decission trees, xgboost and gradient boosting models:

	* .plot		: Generic function to plot the tree of any of the four models with default settings
	* .randomforest : Plot the randomforest model.
	* .xgboost	: Plot the xgboost model.
	* .LightBM	: Plot the LightBM model.


.. |figd| image:: ../figs/fig_breast_randomforest.png

.. table:: Decision tree for breastcancerusing RandomForest.
   :align: center

   +----------+
   | |figd|   |
   +----------+


Sponsor
=======
**This library is created and maintained in my free time**. I like to work on my open-source libraries, and you can help by becoming a sponsor! The easiest way is by simply following me on medium, and it will cost you nothing! Simply go to my `medium profile <https://erdogant.medium.com/>`_ and press "follow". Read more on my `sponsor github page <https://github.com/sponsors/erdogant/>`_ why this is important. This also gives you various other ways to sponsor me!


Star is important too!
======================
If you like this project, **star** this repo at the github page! This is important because only then I know how much you like it :)


Quick install
=============

.. code-block:: console

   pip install treeplot


Github
======
Please report bugs, issues and feature extensions there.
Github, `erdogant/treeplot <https://github.com/erdogant/treeplot/>`_.


Citing treeplot
===============
The bibtex can be found in the right side menu at the `github page <https://github.com/erdogant/treeplot/>`_.


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

* :ref:`genindex`



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. raw:: html

	<hr>
	<center>
		<script async type="text/javascript" src="//cdn.carbonads.com/carbon.js?serve=CEADP27U&placement=erdogantgithubio" id="_carbonads_js"></script>
	</center>
	<hr>

