from spm._runtime import Runtime


def _megplanar_sincos(*args, **kwargs):
    r"""
      This attempts to re-implements Ole's method, exept that the definition of the  
        horizontal and vertical direction is different.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/megplanar_sincos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("megplanar_sincos", *args, **kwargs)
