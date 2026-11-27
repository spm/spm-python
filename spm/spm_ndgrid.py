from spm._runtime import Runtime


def spm_ndgrid(*args, **kwargs):
    r"""
      Return a matrix of grid points in the domain specified by x  
        FORMAT [X,x] = spm_ndgrid(x)  
         
        x{i):   cell array of vectors specifying support or;  
        x(i):   vector of bin numbers in the range [-1 1]  
         
        x{i):   cell array of vectors specifying support or;  
        X:      (n x m) coordinates of n points in m-D space  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ndgrid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ndgrid", *args, **kwargs)
