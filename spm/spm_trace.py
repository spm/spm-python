from spm._runtime import Runtime


def spm_trace(*args, **kwargs):
    r"""
      Fast trace for large matrices: C = spm_trace(A,B) = trace(A*B)  
        FORMAT [C] = spm_trace(A,B)  
         
        C = spm_trace(A,B) = trace(A*B) = sum(sum(A'.*B));  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_trace.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_trace", *args, **kwargs)
