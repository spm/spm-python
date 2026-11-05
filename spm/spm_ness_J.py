from spm._runtime import Runtime


def spm_ness_J(*args, **kwargs):
    r"""
      Return the Jacobian given a polynomial parameterisation  
        FORMAT J = spm_ness_J(P,M,X)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_J.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_J", *args, **kwargs)
