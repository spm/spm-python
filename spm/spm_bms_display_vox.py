from spm._runtime import Runtime


def spm_bms_display_vox(*args, **kwargs):
    r"""
      Display results from BMS Maps at current voxel  
        FORMAT spm_bms_display_vox(BMS,xyz)  
         
        Input:  
        xyz - voxel coordinates [1,3] (voxel)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bms_display_vox.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_display_vox", *args, **kwargs, nargout=0)
