import setuptools
import re

# versioning ------------
VERSIONFILE="treeplot/__init__.py"
getversion = re.search( r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# Setup ------------
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     install_requires=['sklearn','numpy','graphviz','matplotlib','wget'],
     python_requires='>=3',
     name='treeplot',
     version=new_version,
     author="Erdogan Taskesen",
     author_email="erdogant@gmail.com",
     description="Python package treeplot vizualizes a tree based on a randomforest or xgboost model.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/erdogant/treeplot",
	 download_url = 'https://github.com/erdogant/treeplot/archive/'+new_version+'.tar.gz',
     packages=setuptools.find_packages(), # Searches throughout all dirs for files to include
     include_package_data=True, # Must be true to include files depicted in MANIFEST.in
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
