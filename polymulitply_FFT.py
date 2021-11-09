import numpy as np
from random import randint
import time
from FFT import fft, fftI, getComplex


def getV(n):
    return getComplex(n)

def polyMultiply(p, q, n, Varray):
    # pad the 2 numbers with n 0's
    p += [0 for _ in range(n)]
    q += [0 for _ in range(n)]

    # run the 2 'new' numbers through original FFT
    s0 = fft(p, Varray, 2*n)
    s1 = fft(q, Varray, 2*n)

    # Multiply the parts to get the new number
    s = [s0[i]*s1[i] for i in range(2*n)]

    # run the new number through FFT^-1
    interpolate = fftI(s, [], 2*n)
    # extract real number
    realNum = [x.real for x in interpolate]
    # return the rounded number
    return [round(i) for i in realNum]

''' ********** Test VS School Book ***********'''
# print(f"FFT of 21 * 12: {polyMultiply([1, 2], [2, 1], 2, getV(4))}")
# print(f"School Book: {12 * 21}")
# print("==================================================")
# print(f"FFT of 4321 * 8765: {polyMultiply([1, 2, 3, 4], [5, 6, 7, 8], 4, getV(8))}")
# print(f"School Book: {4321 * 8765}")
# print("If array indexes are carried numbers to comply")
# print("==================================================")
    
# Note that the rounded number is not in simplified base 10
# to see the correctly formatted base 10 would need to carry
# the 10's and above

Base = 2**11
def convertBack(digits, base = Base):
    # Initialize result
    digits = list(reversed(digits)) #start at the highest order term
    result = digits[0]
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, len(digits)):
        result = result * base + digits[i]
    return result

def createNum(n):
    return [randint(0,Base-1) for _ in range(n)]

#Test that they find the same answer
n=2**16

'''Test Passes for 2**16'''
Varray = getV(2 * n)
# for _ in range(1):
#     p = createNum(n)
#     q = createNum(n)
#     pq = polyMultiply(p, q, n, Varray)
#     fftAns = convertBack(pq)
#     pythAns = convertBack(p)*convertBack(q)
#     print("FFT answer is    %d" % fftAns)
#     print("Python answer is %d" % pythAns)
#     if not fftAns == pythAns:
#         print("ERROR")
#         x=dfdfdfdf

# test the time:
# timesFFT = []
# timesPol = []
# for _ in range(3):
#     p = createNum(n)
#     q = createNum(n)
#     tic = time.perf_counter()
#     polyMultiply(p, q, n, Varray)
#     toc = time.perf_counter()
#     timesFFT.append(toc - tic)
#     # convert to python rep without timing
#     pn = convertBack(p)
#     qn = convertBack(q)
#     tic = time.perf_counter()
#     pn * qn
#     toc = time.perf_counter()
#     timesPol.append(toc - tic)
# print("FFT    run time is %f" % np.mean(timesFFT))
# print("Python run time is %f" % np.mean(timesPol))
'''Run Time Comparison:
    FFT: 3.142405
    Python: .077117'''
