from spm._runtime import Runtime


def spm_dftmtx(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dftmtx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dftmtx", *args, **kwargs)
