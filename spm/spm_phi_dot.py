from spm._runtime import Runtime


def spm_phi_dot(*args, **kwargs):
    r"""
      Return the derivative of the logistic function  
        FORMAT [y] = spm_phi_dot(x)  
        see spm_phi and spm_inv_phi  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_phi_dot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_phi_dot", *args, **kwargs)
