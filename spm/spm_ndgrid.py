from spm.__wrapper__ import Runtime


def spm_ndgrid(*args, **kwargs):
    """
      Return a matrix of grid points in the domain specified by x  
        FORMAT [X,x] = spm_ndgrid(x)  
         
        x{i):   cell array of vectors specifying support or;  
        x(i):   vector of bin numbers in the range [-1 1]  
         
        x{i):   cell array of vectors specifying support or;  
        X:      (n x m) coordinates of n points in m-D space  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ndgrid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ndgrid", *args, **kwargs)
