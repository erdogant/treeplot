"""Python package treeplot vizualizes a tree based on a randomforest or xgboost model."""
# --------------------------------------------------
# Name        : treeplot.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/treeplot
# Licence     : MIT
# --------------------------------------------------

# %% Libraries
import os
import zipfile
import numpy as np
from xgboost import plot_tree, plot_importance
from sklearn.tree import export_graphviz
from sklearn.datasets import make_classification
from subprocess import call
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from graphviz import Source


# %% Plot tree
def plot(model, featnames=None, num_trees=0, figsize=(25,25), verbose=3):
    """Make tree plot for the input model.

    Parameters
    ----------
    model : model
        xgboost or randomforest model.
    featnames : list, optional
        list of feature names. The default is None.
    num_trees : int, default 0
        Specify the ordinal number of target tree
    figsize: tuple, default (25,25)
        Figure size, (height, width)
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: NONE, 1: ERROR, 2: WARNING, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    None.

    """
    if 'forest' in str(model).lower():
        ax=randomforest(model, featnames=featnames, num_trees=num_trees, figsize=figsize, verbose=verbose)
    if 'xgb' in str(model).lower():
        ax=xgboost(model, featnames=featnames, num_trees=num_trees, figsize=figsize, verbose=verbose)

    return(ax)


# %% Plot tree
def xgboost(model, featnames=None, num_trees=0, plottype='horizontal', figsize=(25,25), verbose=3):
    """Plot tree based on a xgboost.

    Parameters
    ----------
    model : model
        xgboost model.
    featnames : list, optional
        list of feature names. The default is None.
    num_trees : int, default 0
        Specify the ordinal number of target tree
    plottype : str, optional
        Make 'horizontal' or 'vertical' plot. The default is 'horizontal'.
    figsize: tuple, default (25,25)
        Figure size, (height, width)
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: NONE, 1: ERROR, 2: WARNING, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    None.

    """
    if 'xgb' not in str(model).lower():
        raise ImportError('The models seems not to be a xgboost model?')

    if plottype=='horizontal': plottype='UD'
    if plottype=='vertical': plottype='LR'
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    plot_tree(model, num_trees=num_trees, rankdir=plottype, ax=ax)

    # Plot importance
    plot_importance(model)

    return(ax)


# %% Plot tree
def randomforest(model, featnames=None, num_trees=0, filepath='tree', export='png', resolution=100, figsize=(25,25), verbose=3):
    """Plot tree based on a randomforest.

    Parameters
    ----------
    model : model
        randomforest model.
    featnames : list, optional
        list of feature names. The default is None.
    num_trees : int, default 0
        Specify the ordinal number of target tree
    filepath : str, optional
        filename to export. The default is 'tree'.
    export : list of str, optional
        Export type. The default is 'png'.
        Alternatives: 'pdf', 'png'
    resolution : int, optional
        resolution of the png file. The default is 100.
    figsize: tuple, default (25,25)
        Figure size, (height, width)
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: NONE, 1: ERROR, 2: WARNING, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    None.

    """
    ax=None
    if 'forest' not in str(model).lower():
        raise ImportError('The models seems not to be a randomforest model?')
    # Set envirerement
    _set_graphviz_path()
    dotfile = filepath + '.dot'
    pngfile = filepath + '.png'

    if isinstance(featnames, type(None)):
        featnames = np.arange(0,len(model.feature_importances_)).astype(str)

    # Get model parameters
    if hasattr(model, 'estimators_'):
        estimator = model.estimators_[num_trees]
    else:
        estimator = model

    # Make dot file
    dot_data = export_graphviz(estimator,
                               out_file=dotfile,
                               feature_names=featnames,
                               class_names=model.classes_.astype(str),
                               rounded=True,
                               proportion=False,
                               precision=2,
                               filled=True,
                               )

    # Save to pdf
    if export=='pdf':
        s = Source.from_file(dotfile)
        s.view()

    # Save to png
    if export=='png':
        # Convert to png using system command (requires Graphviz)
        call(['dot', '-Tpng', dotfile, '-o', pngfile, '-Gdpi=' + str(resolution)])
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        img = mpimg.imread(pngfile)
        plt.imshow(img)
        plt.axis('off')

    return(ax)


# %% Example data
def import_example(n_samples=1000, n_feat=10):
    """Import Example.

    Parameters
    ----------
    n_samples : int, optional
        Number of samples to generate. The default is 1000.
    n_feat : int, optional
        Number of features to generate. The default is 10.

    Returns
    -------
    None.

    """
    [X, y] = make_classification(n_samples=n_samples, n_features=n_feat)
    return(X,y)


# %% Get graphiz path and include into local PATH
def _set_graphviz_path(gfile='graphviz-2.38.zip', verbose=3):
    curpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RESOURCES')
    # filesindir = os.listdir(curpath)[0]
    idx = gfile[::-1].find('.') + 1
    dirname = gfile[:-idx]
    getPath = os.path.abspath(os.path.join(curpath, dirname))
    getZip = os.path.abspath(os.path.join(curpath, gfile))
    # Unzip if path does not exists
    if not os.path.isdir(getPath):
        if verbose>=3: print('[TREEPLOT] Extracting graphviz files..')
        [pathname, _] = os.path.split(getZip)
        # Unzip
        zip_ref = zipfile.ZipFile(getZip, 'r')
        zip_ref.extractall(pathname)
        zip_ref.close()
        getPath = os.path.join(pathname, dirname)

    # Point directly to the bin
    finPath = os.path.abspath(os.path.join(getPath, 'release', 'bin'))

    # Add to system
    if finPath not in os.environ["PATH"]:
        if verbose>=3: print('[TREEPLOT] Set path in environment.')
        os.environ["PATH"] += os.pathsep + finPath

    return(finPath)
