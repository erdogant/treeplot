import treeplot
print(dir(treeplot))
print(treeplot.__version__)


# %% Make example dataset
X,y = treeplot.import_example('breast')


# %% RF EXAMPLE
from sklearn.tree import DecisionTreeClassifier
model_rf = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)

ax = treeplot.randomforest(model_rf)


# %% RF EXAMPLE
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.randomforest(model, export='png')
ax = treeplot.randomforest(model, export='pdf')

# %%
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
gb = GradientBoostingClassifier()
model = gb.fit(X, y)

ax = treeplot.plot(model)

# %% EXAMPLE XGBOOST
from xgboost import XGBClassifier
model_xgb = XGBClassifier(n_estimators=100, max_depth=2, random_state=0).fit(X, y)

ax = treeplot.xgboost(model_xgb)
ax = treeplot.xgboost(model_xgb, plottype='vertical')

# %% Auto detect model
ax = treeplot.plot(model_xgb)
ax = treeplot.plot(model_rf)
