from spm.__wrapper__ import Runtime


def spm_vecfun(*args, **kwargs):
    """
      Apply a function to the numeric elements of a cell or structure array  
        FORMAT [X] = spm_vecfun(X,fun)  
        X   - numeric, cell or stucture array  
        fun - function handle  
       __________________________________________________________________________  
         
        e.g., pE = spm_vecfun(pE,@log)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vecfun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vecfun", *args, **kwargs)
