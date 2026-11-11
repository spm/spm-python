from spm._runtime import Runtime


def spm_hilbert(*args, **kwargs):
    r"""
      Computes analytic signal  
        FORMAT [x] = spm_hilbert(xr)  
         
        Returns analytic signal x = xr + i*xi such that xi is the Hilbert  
        transform of real vector xr.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_hilbert.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_hilbert", *args, **kwargs)
