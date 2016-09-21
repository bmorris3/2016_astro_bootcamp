# 2016 Python Bootcamp for Astronomy and Physics

Sept 26-27, 2016 in PAA 216

Visit the bootcamp website [here](https://bmorris3.github.io/2016_astro_bootcamp/).

Welcome to Python Bootcamp - a highly-condensed, fast-paced, incomplete tour of the Python language and some of its essential packages used in physics and astronomy with Python. This course is meant for students who are experienced programmers in a language other than Python. We will give you broad and shallow exposure to the plethora of tools that may be useful to you in Python, starting at the basics of the language and moving up to scientific computation in Python.

### Topics

In this two-day "course", we'll introduce you to:
* efficient calculations with numpy
* visualization with matplotlib
* writing functions and modules
* optimization with numpy and scipy
* object-oriented programming
* handling "big data" with HDF5
* astronomical calculations with astropy
* version control and collaboration with git and GitHub

### Getting set up for Bootcamp

Before arriving at Bootcamp, we will assume that you have Python and the required packages installed. The easiest way to do that (and I _very strongly_ encourage that you do it this way) is to use the **Anaconda** package manager. [Download and install Anaconda](https://www.continuum.io/downloads) (or [miniconda](http://conda.pydata.org/miniconda.html) if disk space is a concern) **for Python 3**, and then install the dependencies for this course with the following command in your terminal: 
```bash 
conda install numpy scipy astropy matplotlib h5py jupyter ipython
conda install -c astropy astroquery
```
This will download and install all of the required dependencies for our tutorials. Contact me if you have trouble getting set up _before_ bootcamp begins (but be warned: I will only provide installation support if you're using anaconda)! If you plan to stick around for the git tutorial, you should also install [git](https://git-scm.com/downloads).

#### Testing your setup

You can test if you've successfully installed Python and the required depedencies by doing the following. 

* Open a new terminal window, and type `ipython`. This will open an interactive iPython shell, giving you a prompt that says `In [1]:`.
* Copy this code to your clipboard: 
```python
import numpy
import scipy
import astropy
import matplotlib
import h5py
import astroquery
```
* Type into the iPython shell the word `paste`, and press enter.
* If no errors are raised, you're ready for bootcamp. You may close the terminal window.

### Instructor

[Brett Morris](http://brettmorr.is) is a fourth-year graduate student of Astronomy and Astrobiology. He maintains the astropy-affiliated package [astroplan](http://github.com/astropy/astroplan/), among others.

### Resources

In addition to the notebooks in this repository, we will use Jake Vanderplas' 2014 Python Bootcamp notebooks, which I've forked [here](https://github.com/bmorris3/2014_fall_ASTR599).

#### Further reading

For additional resources on getting up to speed in Python, I recommend Jake's book _A Whirlwind Tour of Python_, which is [currently available for free](http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf). If you're ready to go deeper, there are [many freely available books on Python to try](http://pythonbooks.revolunet.com).

### Preliminary schedule

|Time | Lesson | 
|-----|-----|
| Mon 9-10:30 | Basic training | 
| Mon 10:30-11:30 | Data structures |
| Mon 11:30-12  | iPython | 
| Mon 1-2 | Functions, modules | 
| Mon 2-3:30 | Git intro |
| Tues 9-10:30 | Numpy intro | 
| Tues 10:00-10:30 | Matplotlib intro | 
| Tues 10:30-11:30 | Optimization intro | 
| Tues 1-2 | Intro to astropy |
| Tues 2-3 | Intro to OO | 
| Tues 3-4 | Intro to HDF5 | 
| Tues 3-4 | GitHub intro |
