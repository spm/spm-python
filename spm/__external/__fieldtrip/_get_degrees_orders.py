from spm._runtime import Runtime


def _get_degrees_orders(*args, **kwargs):
    r"""
      this helper function assumes the order of the basis vectors, as computed  
        in the MNE-Python implementation is the same as the order of the basis  
        vectors as computed in the SPM implementation  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/get_degrees_orders.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("get_degrees_orders", *args, **kwargs)
