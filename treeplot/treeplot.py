"""Python package treeplot vizualizes a tree based on a randomforest or xgboost model."""
# --------------------------------------------------
# Name        : treeplot.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/treeplot
# Licence     : See Licences
# --------------------------------------------------

# %% Libraries
import os
import sys
import zipfile
import numpy as np
from sklearn.tree import export_graphviz
# from sklearn.tree.export import export_text
from sklearn.tree import export_text
from subprocess import call
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from graphviz import Source
import wget
URL = 'https://erdogant.github.io/datasets/graphviz-2.38.zip'


# %% Plot tree
def plot(model, featnames=None, num_trees=None, plottype='horizontal', figsize=(25,25), verbose=3):
    """Make tree plot for the input model.

    Parameters
    ----------
    model : model
        xgboost or randomforest model.
    featnames : list, optional
        list of feature names. The default is None.
    num_trees : int, default None
        The best performing tree is choosen. Specify any other ordinal number for another target tree
    plottype : str, (default : 'horizontal')
        Works only in case of xgb model.
        * 'horizontal'
        * 'vertical'
    figsize: tuple, default (25,25)
        Figure size, (height, width)
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: NONE, 1: ERROR, 2: WARNING, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    ax : Figure axis
        Figure axis of the input model.

    """
    modelname = str(model).lower()
    if ('xgb' in modelname):
        if verbose>=4: print('xgboost plotting pipeline.')
        ax = xgboost(model, featnames=featnames, num_trees=num_trees, figsize=figsize, plottype=plottype, verbose=verbose)
    elif ('tree' in modelname) or ('forest' in modelname) or ('gradientboosting' in modelname):
        if verbose>=4: print('tree plotting pipeline.')
        ax = randomforest(model, featnames=featnames, num_trees=num_trees, figsize=figsize, verbose=verbose)
    elif ('lgb' in modelname):
        ax = lgbm(model, featnames=featnames, num_trees=num_trees, figsize=figsize, verbose=verbose)
    else:
        print('[treeplot] >Model not recognized: %s' %(modelname))
        ax = None

    return ax


# %% Plot tree
def lgbm(model, featnames=None, num_trees=None, figsize=(25,25), verbose=3):
    try:
        from lightgbm import plot_tree, plot_importance
    except:
        if verbose>=1: raise ImportError('lightgbm must be installed. Try to: <pip install lightgbm>')
        return None

    # Check model
    _check_model(model, 'lgb')
    # Set env
    _set_graphviz_path()

    if (num_trees is None) and hasattr(model, 'best_iteration_'):
        num_trees = model.best_iteration_
        if verbose>=3: print('[treeplot] >Best detected tree: %.0d' %(num_trees))
    elif num_trees is None:
        num_trees = 0
    
    ax1 = None
    try:
        fig, ax1 = plt.subplots(1, 1, figsize=figsize)
        plot_tree(model, tree_index=num_trees, dpi=200, ax=ax1)
    except:
        if _get_platform() != "windows":
            print('[treeplot] >Install graphviz first: <sudo apt install python-pydot python-pydot-ng graphviz>')

    # Plot importance
    ax2 = None
    try:
        fig, ax2 = plt.subplots(1, 1, figsize=figsize)
        plot_importance(model, max_num_features=50, ax=ax2)
    except:
        print('[treeplot] >Error: importance can not be plotted. Booster.get_score() results in empty. This maybe caused by having all trees as decision dumps.')

    return(ax1, ax2)

# %% Plot tree
def xgboost(model, featnames=None, num_trees=None, plottype='horizontal', figsize=(25,25), verbose=3):
    """Plot tree based on a xgboost.

    Parameters
    ----------
    model : model
        xgboost model.
    featnames : list, optional
        list of feature names. The default is None.
    num_trees : int, default None
        The best performing tree is choosen. Specify any other ordinal number for another target tree
    plottype : str, optional
        Make 'horizontal' or 'vertical' plot. The default is 'horizontal'.
    figsize: tuple, default (25,25)
        Figure size, (height, width)
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: NONE, 1: ERROR, 2: WARNING, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    ax : Figure axis
        Figure axis of the input model.

    """
    try:
        from xgboost import plot_tree, plot_importance
    except:
        if verbose>=1: raise ImportError('xgboost must be installed. Try to: <pip install xgboost>')

    _check_model(model, 'xgb')
    # Set env
    _set_graphviz_path()

    if plottype=='horizontal': plottype='UD'
    if plottype=='vertical': plottype='LR'
    if (num_trees is None) and hasattr(model, 'best_iteration'):
        num_trees = model.best_iteration
        if verbose>=3: print('[treeplot] >Best detected tree: %.0d' %(num_trees))
    elif num_trees is None:
        num_trees = 0

    ax1 = None
    try:
        fig, ax1 = plt.subplots(1, 1, figsize=figsize)
        plot_tree(model, num_trees=num_trees, rankdir=plottype, ax=ax1)
    except:
        if _get_platform() != "windows":
            print('[treeplot] >Install graphviz first: <sudo apt install python-pydot python-pydot-ng graphviz>')

    # Plot importance
    ax2 = None
    try:
        fig, ax2 = plt.subplots(1, 1, figsize=figsize)
        plot_importance(model, max_num_features=50, ax=ax2)
    except:
        print('[treeplot] >Error: importance can not be plotted. Booster.get_score() results in empty. This maybe caused by having all trees as decision dumps.')

    return(ax1, ax2)


# %% Plot tree
def randomforest(model, featnames=None, num_trees=None, filepath='tree', export='png', resolution=100, figsize=(25,25), verbose=3):
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
    ax : Figure axis
        Figure axis of the input model.

    """
    ax=None
    dotfile = None
    pngfile = None
    if num_trees is None: num_trees = 0

    # Check model
    _check_model(model, 'randomforest')
    # Set env
    _set_graphviz_path()

    if export is not None:
        dotfile = filepath + '.dot'
        pngfile = filepath + '.png'

    if featnames is None:
        featnames = np.arange(0,len(model.feature_importances_)).astype(str)

    # Get model parameters
    if ('gradientboosting' in str(model).lower()):
        estimator = model.estimators_[num_trees][0]
    else:
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
    if export == 'pdf':
        s = Source.from_file(dotfile)
        s.view()
    # Save to png
    elif export == 'png':
        try:
            call(['dot', '-Tpng', dotfile, '-o', pngfile, '-Gdpi=' + str(resolution)])
            fig, ax = plt.subplots(1, 1, figsize=figsize)
            img = mpimg.imread(pngfile)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
        except:
            if _get_platform() != "windows":
                print('[treeplot] >Install graphviz first: <sudo apt install python-pydot python-pydot-ng graphviz>')
    else:
        graph = Source(dot_data)
        plt.show()

    return(ax)


# %% Import example dataset from github.
def import_example(data='random', n_samples=1000, n_feat=10):
    """Import example dataset from sklearn.

    Parameters
    ----------
    data : str
        'random' : str, two-class
        'breast' : str, two-class
        'titanic': str, two-class
        'iris' : str, multi-class
    n_samples : int, optional
        Number of samples to generate. The default is 1000.
    n_feat : int, optional
        Number of features to generate. The default is 10.

    Returns
    -------
    tuple (X,y).
        X is the dataset and y the response variable.

    """
    try:
        from sklearn import datasets
    except:
        print('This requires: <pip install sklearn>')
        return None, None

    if data=='iris':
        X, y = datasets.load_iris(return_X_y=True)
    elif data=='breast':
        X, y = datasets.load_breast_cancer(return_X_y=True)
    elif data=='titanic':
        X, y = datasets.fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    elif data=='random':
        X, y = datasets.make_classification(n_samples=n_samples, n_features=n_feat)

    return X, y


# %% Get graphiz path and include into local PATH
def _set_graphviz_path(verbose=3):
    finPath=''
    if _get_platform()=="windows":
        # Download from github
        [gfile, curpath] = _download_graphviz(URL, verbose=verbose)

        # curpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RESOURCES')
        # filesindir = os.listdir(curpath)[0]
        idx = gfile[::-1].find('.') + 1
        dirname = gfile[:-idx]
        getPath = os.path.abspath(os.path.join(curpath, dirname))
        getZip = os.path.abspath(os.path.join(curpath, gfile))
        # Unzip if path does not exists
        if not os.path.isdir(getPath):
            if verbose>=3: print('[treeplot] >Extracting graphviz files..')
            [pathname, _] = os.path.split(getZip)
            # Unzip
            zip_ref = zipfile.ZipFile(getZip, 'r')
            zip_ref.extractall(pathname)
            zip_ref.close()
            getPath = os.path.join(pathname, dirname)

        # Point directly to the bin
        finPath = os.path.abspath(os.path.join(getPath, 'release', 'bin'))
    else:
        pass
        # sudo apt install python-pydot python-pydot-ng graphviz
        # dpkg -l | grep graphviz
        # call(['dpkg', '-l', 'grep', 'graphviz'])
        # call(['dpkg', '-s', 'graphviz'])

    # Add to system
    if finPath not in os.environ["PATH"]:
        if verbose>=3: print('[treeplot] >Set path in environment.')
        os.environ["PATH"] += os.pathsep + finPath

    return(finPath)


# %%
def _get_platform():
    platforms = {
        'linux1':'linux',
        'linux2':'linux',
        'darwin':'osx',
        'win32':'windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]


# %% Check input model
def _check_model(model, expected):
    modelname = str(model).lower()
    if (expected=='randomforest'):
        if ('forest' in modelname) or ('tree' in modelname) or ('gradientboosting' in modelname):
            pass
        else:
            print('[treeplot] >>Warning: The input model seems not to be a tree-based model?')
    if (expected=='xgb'):
        if ('xgb' not in modelname):
            print('[treeplot] >Warning: The input model seems not to be a xgboost model?')
    if (expected=='lgb'):
        if ('lgb' not in modelname):
            print('[treeplot] >Warning: The input model seems not to be a lightgbm model?')

# %% Import example dataset from github.
def _download_graphviz(url, verbose=3):
    """Import example dataset from github.

    Parameters
    ----------
    url : str, optional
        url-Link to graphviz. The default is 'https://erdogant.github.io/datasets/graphviz-2.38.zip'.
    verbose : int, optional
        Print message to screen. The default is 3.

    Returns
    -------
    tuple : (gfile, curpath).
        gfile : filename
        curpath : currentpath

    """
    curpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RESOURCES')
    gfile = wget.filename_from_url(url)
    PATH_TO_DATA = os.path.join(curpath, gfile)
    if not os.path.isdir(curpath):
        if verbose>=3: print('[treeplot] >Downloading graphviz..')
        os.makedirs(curpath, exist_ok=True)

    # Check file exists.
    if not os.path.isfile(PATH_TO_DATA):
        # Download data from URL
        if verbose>=3: print('[treeplot] >Downloading graphviz..')
        wget.download(url, curpath)

    return(gfile, curpath)
