from spm._runtime import Runtime


def fil_subvol(*args, **kwargs):
    r"""
      Dimensions and voxel-to world mapping of a subvolume  
        FORMAT [d,M] = fil_subvol(Nii,bb)  
        Nii    - SPM NIfTI object  
        bb     - bounding box (2 x 3)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/fil_subvol.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fil_subvol", *args, **kwargs)
