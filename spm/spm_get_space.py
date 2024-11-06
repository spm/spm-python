from spm.__wrapper__ import Runtime


def spm_get_space(*args, **kwargs):
    """
      Get/set the voxel-to-world mapping of an image  
        FORMAT M = spm_get_space(P)  
                   spm_get_space(P,M)  
        P - image filename  
        M - voxel-to-world mapping  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_space.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_space", *args, **kwargs)
