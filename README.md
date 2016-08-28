# 2016 Python Bootcamp for Astronomy and Physics

Sept 26-27, 2016 in PAA 216

Welcome to Python Bootcamp - a highly-condensed, fast-paced, incomplete tour of the Python language and some of its essential packages used in physics and astronomy with Python. In this two-day course, we'll introduce you to:
* efficient calculations with numpy
* visualization with matplotlib
* writing functions and modules
* optimization with numpy and scipy
* object-oriented programming
* handling "big data" with HDF5
* astronomical calculations with astropy

### Getting set up for Bootcamp

Before arriving at Bootcamp, we will assume that you have Python and the required packages installed. The easiest way to do that (and I _very strongly_ encourage that you do it this way) is to use the **Anaconda** package manager. [Download and install Anaconda](https://www.continuum.io/downloads) (or [miniconda](http://conda.pydata.org/miniconda.html) if disk space is a concern) **for Python 3**, and then install the dependencies for this course with the following command in your terminal: 
```bash 
conda install numpy scipy astropy matplotlib h5py jupyter
```
This will download and install all of the required dependencies for our tutorials. Contact me if you have trouble getting set up _before_ bootcamp begins! You may also want to install `git` if you don't already have it installed, as all of our lessons are accessible via GitHub.

### Instructor

[Brett Morris](http://brettmorr.is) is a fourth-year graduate student of Astronomy and Astrobiology. He maintains the astropy-affiliated package [astroplan](http://github.com/astropy/astroplan/), among others.

### Resources

In addition to the notebooks in this repository, we will use Jake Vanderplas' 2014 Python Bootcamp notebooks, which I've forked [here](https://github.com/bmorris3/2014_fall_ASTR599).

#### Further reading

For additional resources on Python, I recommend Jake's book _A Whirlwind Tour of Python_, which is [currently available for free](](http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf)).
