from spm.__wrapper__ import Runtime


def spm_A_reduce(*args, **kwargs):
    """
      Reduction of Markovian partition  
        FORMAT [J,z,v,s] = spm_A_reduce(J,x,T,N)  
        J  - Jacobian (x)  
        x  - {3 x n}  particular partition of states  
        T  - eigenvalue threshold to retain eigenvectors [default: 8]  
        N  - maximum number to retain [default: 8]  
         
        J  - Jacobian (z)  
        z  - {1 x n} partition of states at the next level  
        v  - {1 x n} eigenvector (adiabatic) operator  
        s  - {1 x n} eigenvalues  
         
        Adiabatic reduction operator (R)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_A_reduce.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_A_reduce", *args, **kwargs)
