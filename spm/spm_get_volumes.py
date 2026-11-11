from spm._runtime import Runtime


def spm_get_volumes(*args, **kwargs):
    r"""
      Compute total volumes from tissue segmentations  
        FORMAT gl = spm_get_volumes(P)  
        P  - a matrix of image filenames  
        gl - a vector of volumes (in litres)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_get_volumes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_volumes", *args, **kwargs)
