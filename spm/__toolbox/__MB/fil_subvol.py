from spm.__wrapper__ import Runtime


def fil_subvol(*args, **kwargs):
    """
      Dimensions and voxel-to world mapping of a subvolume  
        FORMAT [d,M] = fil_subvol(Nii,bb)  
        Nii    - SPM NIfTI object  
        bb     - bounding box (2 x 3)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_subvol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_subvol", *args, **kwargs)
