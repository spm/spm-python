from spm._runtime import Runtime


def spm_vecfun(*args, **kwargs):
    r"""
      Apply a function to the numeric elements of a cell or structure array  
        FORMAT [X] = spm_vecfun(X,fun)  
        X   - numeric, cell or stucture array  
        fun - function handle  
       __________________________________________________________________________  
         
        e.g., pE = spm_vecfun(pE,@log)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vecfun.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vecfun", *args, **kwargs)
