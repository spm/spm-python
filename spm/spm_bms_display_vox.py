from spm.__wrapper__ import Runtime


def spm_bms_display_vox(*args, **kwargs):
    """
      Display results from BMS Maps at current voxel  
        FORMAT spm_bms_display_vox(BMS,xyz)  
         
        Input:  
        xyz - voxel coordinates [1,3] (voxel)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_display_vox.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bms_display_vox", *args, **kwargs, nargout=0)
