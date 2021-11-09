from FFT import getComplex
from polyMul import poly3, polySchool
from polymulitply_FFT import polyMultiply, createNum
import datetime
import sys
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def schoolTime(n):
    a = createNum(n)
    b = createNum(n)
    polySchool(a, b)

def poly3Time(n):
    a = createNum(n)
    b = createNum(n)
    poly3(a, b)

def fftTime(n):
    a = createNum(n)
    b = createNum(n)
    polyMultiply(a, b, n, getComplex(n*2))

empTL = []
empS = []
for n in [2**5, 2**6, 2**7, 2**8]:
    startTime = datetime.datetime.now()
    schoolTime(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: #sometimes the function is too fast and we get 0 time
        empTL.append(elapsed)
        empS.append(n)

poly3TL = []
poly3S = []
for n in [2**6, 2**7, 2**8, 2**9]:
    startTime = datetime.datetime.now()
    poly3Time(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: #sometimes the function is too fast and we get 0 time
        poly3TL.append(elapsed)
        poly3S.append(n)

fftTL = []
fftS = []
sizes = [2**i for i in range(7, 26)]
for n in sizes:
    startTime = datetime.datetime.now()
    fftTime(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: #sometimes the function is too fast and we get 0 time
        fftTL.append(elapsed)
        fftS.append(n)


plt.xlabel("n")
plt.ylabel("time in milliseconds")
plt.yscale('log')
plt.xscale('log')

plt.plot(empS, empTL, 'g')
plt.plot(poly3S, poly3TL, 'b')
plt.plot(fftS, fftTL, 'r')


plt.rcParams["figure.figsize"] = [16,9]
plt.show()

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in empS], [np.log(t) for t in empTL])
print("School Book Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in poly3S], [np.log(t) for t in poly3TL])
print("Poly 3 Sub Parts Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in fftS], [np.log(t) for t in fftTL])
print("FFT Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

