from spm._runtime import Runtime


def _lbex(*args, **kwargs):
    r"""
      This function will add the field "subspace" to the sourcemodel definition.  
         
        The subspace projection is based on the LBEX (local basis expansion)  
        method.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/lbex.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("lbex", *args, **kwargs)
