from FFT import getComplex
from polyMul import poly3, polySchool
from polymulitply_FFT import convertBack, polyMultiply, createNum
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

def pythonTime(n):
    a = createNum(n)
    b = createNum(n)
    an = convertBack(a)
    bn = convertBack(b)
    an * bn

empTL = []
empS = []
sizes = [2**i for i in range(5, 13)]
for n in sizes:
    startTime = datetime.datetime.now()
    schoolTime(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: 
        empTL.append(elapsed)
        empS.append(n)

poly3TL = []
poly3S = []
sizes = [2**i for i in range(7, 13)]
for n in sizes:
    startTime = datetime.datetime.now()
    poly3Time(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: 
        poly3TL.append(elapsed)
        poly3S.append(n)

fftTL = []
fftS = []
sizes = [2**i for i in range(7, 17)]
for n in sizes:
    startTime = datetime.datetime.now()
    fftTime(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: 
        fftTL.append(elapsed)
        fftS.append(n)


pythonTL = []
pythonS = []
sizes = [2**i for i in range(7, 18)]
for n in sizes:
    startTime = datetime.datetime.now()
    pythonTime(n)
    endTime = datetime.datetime.now()
    time_diff = (endTime - startTime)
    elapsed = time_diff.total_seconds() * 1000
    if elapsed > 0: 
        pythonTL.append(elapsed)
        pythonS.append(n)


plt.xlabel("n")
plt.ylabel("time in milliseconds")
plt.yscale('log')
plt.xscale('log')

plt.plot(empS, empTL, 'g')
plt.plot(poly3S, poly3TL, 'b')
plt.plot(fftS, fftTL, 'r')
plt.plot(pythonS, pythonTL, 'b')


plt.rcParams["figure.figsize"] = [16,9]
plt.show()

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in empS], [np.log(t) for t in empTL])
print("School Book Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in poly3S], [np.log(t) for t in poly3TL])
print("Poly 3 Sub Parts Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in fftS], [np.log(t) for t in fftTL])
print("FFT Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in pythonS], [np.log(t) for t in pythonTL])
print("Python Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

