from spm.__wrapper__ import Runtime


def spm_dftmtx(*args, **kwargs):
    """
      Create basis functions for Discrete Cosine Transform  
        FORMAT C = spm_dftmtx(N,K,a)  
         
        N - dimension  
        K - order  
        a - number of (1/2)5Hz frequency steps (default a = 2)  
       __________________________________________________________________________  
        spm_dftmtx creates a matrix for the first few basis functions of a one  
        dimensional discrete Fourier transform.  
         
        See:    Fundamentals of Digital Image Processing (p 150-154).  
                Anil K. Jain 1989.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dftmtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dftmtx", *args, **kwargs)
