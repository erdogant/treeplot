import treeplot
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def test_randomforest():
    X,y = treeplot.import_example()
    model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
    # TEST 1: check output is unchanged
    ax = treeplot.randomforest(model, export='png')
    assert 'matplotlib' not in str(ax)


def test_xgboost():
    X,y = treeplot.import_example()
    model = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)
    # TEST 1: check output is unchanged
    ax = treeplot.xgboost(model)
    assert 'matplotlib' not in str(ax)
