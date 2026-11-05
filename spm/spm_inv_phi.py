from spm._runtime import Runtime


def spm_inv_phi(*args, **kwargs):
    r"""
      Inverse logistic function  
        FORMAT [y] = spm_inv_phi(x)  
         
        x   = log((y./(1 - y))  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_inv_phi.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_inv_phi", *args, **kwargs)
