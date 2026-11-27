from spm._runtime import Runtime


def _settang(*args, **kwargs):
    r"""
      set the dipole cartesian direction, given:  
        1) the instantenious decomposition vectors tanu and tanv  
        2) the instanteneous dipole orientation theta  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/inverse/private/settang.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("settang", *args, **kwargs)
