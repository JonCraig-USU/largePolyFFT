import numpy as np
from nimTime import showTime

# Create the omega values
def getComplex(n):
    w = [complex(np.cos(2*np.pi * i/n), np.sin(2*np.pi * i/n)) for i in range(n)]
    return w

# Main FFT function
def fft(p, w, n):
    # top call
    if w == []:
        w = getComplex(n)

    # Base case to end recursion
    if n == 1:
        return p
    
    # seperate the odd and even terms
    Pe = [p[i] for i in range(0, n, 2)]
    Po = [p[i] for i in range(1, n, 2)]

    # find the new omega values
    wNew = [w[i] * w[i] for i in range(n//2)]

    # 2 recursive calls
    sole = fft(Pe, wNew, n//2)
    solo = fft(Po, wNew, n//2)

    # solution construction and final return
    return [sole[i] + w[i] * solo[i] for i in range(n//2)] + [sole[i] - w[i] * solo[i] for i in range(n//2)]

# Inverse is the same as
def fftI(p, w, n):
    if w == []:
        w = [complex(np.cos(2*np.pi * i/n), -np.sin(2*np.pi * i/n)) for i in range(n)]
    sol = fft(p, w, n)
    return [sol[i] / 8 for i in range(n)]

# test the function
def runTime(n):
    p = [i for i in range(n)]
    w = []
    n = len(p)
    fft(p, w, n)

sizes = [2**i for i in range(7, 26)]

showTime(runTime, sizes, fit='polynomial')


# print("FFT: " + str(fft(p, w, n)))
# print("Flann: " + "out=[(28+0j), (-4.000000000000002-9.65685424949238j), (-4-4j), (-4-1.6568542494923797j), (-4+0j), (-4+1.6568542494923806j), (-3.9999999999999996+4j), (-3.9999999999999982+9.65685424949238j)]")
# print("==================================================================================================================================================================================================================================================================")
# print("FFT Inverse: " + str(fftI(fft(p,w,n), w, n)))
# print("Flann: [1.1102230246251565e-16j, (1-1.6653345369377348e-16j), (2+3.2162452993532727e-16j), (3.0000000000000004+1.6653345369377348e-16j), (4-1.1102230246251565e-16j), (5-1.6653345369377348e-16j), (6-3.2162452993532727e-16j), (7+1.6653345369377348e-16j)]")
# print("==================================================================================================================================================================================================================================================================")


# showTime(function=, sizes=, init=, fit='exponential')
