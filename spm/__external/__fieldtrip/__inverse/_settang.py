from spm._runtime import Runtime


def _settang(*args, **kwargs):
    """
      set the dipole cartesian direction, given:  
        1) the instantenious decomposition vectors tanu and tanv  
        2) the instanteneous dipole orientation theta  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/settang.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("settang", *args, **kwargs)
