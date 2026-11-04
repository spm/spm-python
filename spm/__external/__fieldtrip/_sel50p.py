from spm._runtime import Runtime


def _sel50p(*args, **kwargs):
    r"""
      This function will add the field "subspace" to the grid definition.  
         
        The subspace projection corresponds to selecting 50% of the   
        channels that are the closest to the dipole.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/sel50p.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("sel50p", *args, **kwargs)
