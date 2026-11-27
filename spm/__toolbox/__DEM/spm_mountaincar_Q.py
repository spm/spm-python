from spm._runtime import Runtime


def spm_mountaincar_Q(*args, **kwargs):
    r"""
      Desired ensemble density  
        FORMAT [Q] = spm_mountaincar_Q(x)  
         
        x:  (n x m) matrix of n m-D point in states space  
         
        Q   - desired equilibrium density; p(x)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_mountaincar_Q.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mountaincar_Q", *args, **kwargs)
