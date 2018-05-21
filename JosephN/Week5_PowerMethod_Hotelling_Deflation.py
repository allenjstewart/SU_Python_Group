# -*- coding: utf-8 -*-
"""
Created on Mon May 21 07:48:22 2018

@author: Joey
"""

# AUTHOR: J. Nakao
# DATE: 22 May 2018
# PURPOSE: Power Method and Hotelling Deflation to find dominant eigenvalue/eigenvector pairs.
# INSTRUCTIONS: 
# 1. Define a square matrix as MAT.
# 2. Run code.
# COMMENTS: N/A
# 
# 
import numpy as np
import time as tm
import array as ay

# Matrix to find eigenvalues and eigenvectors
MAT = np.matrix('2 3 5 6; 3 -1 -2 -3; 5 -2 0 2; 6 -3 2 22')

def Power(A):
    n = A.shape[1] #number of columns.
    EigVals = ay.array('f',[]) #eigenvalues.
    for i in range(0,int(n)):
        x0 = np.ones(n)
        x0 = np.asmatrix(x0) #converting array into matrix type.
        x0 = np.transpose(x0) #converting 1xn to nx1.
        tol = 1 #tolerance; starting difference between first two x-vectors.
        while tol > 10**(-9):
            y = A*x0
            eigval = 0 #starting eigenvalue
            for j in range(0,int(n)):
                if np.abs(y[j,0]) >= np.abs(eigval):
                    eigval = y[j,0]
            x = y/eigval
            tol = np.linalg.norm(x - x0) #difference between consecutive x-vectors.
            x0 = x
        eigenvalue = eigval
        eigenvector = x0/np.linalg.norm(x0)
        EigVals.append(eigenvalue)
        if i == 0:
            eigenvector = np.transpose(eigenvector) #transpose to add to set of eigenvectors.
            EigVecs = eigenvector
            eigenvector = np.transpose(eigenvector) #undo transpose.
            A = A - (eigenvalue/float(np.dot(np.transpose(eigenvector),eigenvector)))*np.dot(eigenvector,np.transpose(eigenvector))
        elif i > 0:
            EigVecs = np.vstack((EigVecs,np.transpose(eigenvector)))
            A = A - (eigenvalue/float(np.dot(np.transpose(eigenvector),eigenvector)))*np.dot(eigenvector,np.transpose(eigenvector))  
    #print(EigVals) #all eigenvalues.
    #print(np.transpose(EigVecs)) #eigenvectors as columns.
    EigPairs = {}
    for k in range(0,int(n)):
        EigPairs[EigVals[k]] = EigVecs[k]
    print(EigPairs)

Power(MAT)