import numpy as np

def poly3(p, q):
    l = len(p)  # length of the 2 matrices
    ans = np.zeros(2 * l -1)

    if l == 1:
        ans[0] = p[0] * q[0]
        return ans
    
    elif l == 2:
        ans[0] = p[0] * q[0]
        ans[1] = p[0] * q[1] + p[1] * q[0]
        ans[2] = p[1] * q[1]
        return ans

    else:
        # recurrsive calls for the 4 sub parts 
        low = poly3(p[0:l//2], q[0:l//2])        # low terms are the x**0 indexes to the midway
        middleA = poly3(p[0:l//2], q[l//2:l])   # inside term of foil
        middleB = poly3(p[l//2:l], q[0:l//2])   # insider term of foil
        high = poly3(p[l//2:l], q[l//2:l])     # high terms are the midpoint to the end of the array
        
        # Pad all the arrays so that they match the length of answer
        half = int(l//2)
        low = np.append(low, np.zeros(l))
        middleA = np.append(np.zeros(half), middleA)
        middleA = np.append(middleA, np.zeros(half))
        middleB = np.append(np.zeros(half), middleB)
        middleB = np.append(middleB, np.zeros(half)) 
        high = np.append(np.zeros(l), high)

        # update the answer array
        ans = np.add(ans, low)
        ans = np.add(ans, middleA)
        ans = np.add(ans, middleB)
        ans = np.add(ans, high)

        # return updated array back up the chain
        return ans
# def mult3(p, q, n):
#     m = n // 2
#     if n == 1:
#         return p * q
#     else:
#         ans = np.zeros(2*n-1)
#         pHigh = p[m:n-1]
#         pLow = p[0:m-1]
#         qHigh = q[m:n-1]
#         qLow = q[0:m-1]
#         temp1 = mult3(pHigh+pLow, qHigh+qLow, m)
#         temp2 = mult3(pHigh, qHigh, m)
#         temp3 = mult3(pLow, qLow, m)
#         return

def polySchool(p, q):
    ans = np.zeros(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            ans[i+j] += p[i] * q[j]
    return ans