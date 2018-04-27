import numpy as np
import re
import os
import itertools
import sys, getopt
from subprocess import call
import subprocess
import json
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
from sklearn.model_selection import train_test_split
from shutil import copyfile
from scipy.optimize import curve_fit
from scipy.special import expit
from scipy.stats.distributions import  t
from sklearn.gaussian_process.kernels import WhiteKernel, ExpSineSquared
from matplotlib import pyplot as plt
from scipy import stats



def func(x, a, b, c):
	return a * np.exp(-b * x) + c

def predict(x_val, slope, intercept):
	return intercept + (slope * x_val)


xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
print(y)
y_noise = 0.5 * np.random.normal(size=xdata.size)
ydata = y + y_noise


popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-')

plt.plot(xdata, ydata, 'b-', label='data')
plt.show()
